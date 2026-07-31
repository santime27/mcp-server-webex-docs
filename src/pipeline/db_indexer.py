import re
import os
import sqlite3
from src.models.db import Domain, Category, Endpoint, get_session, init_db, get_default_db_path

def parse_md_for_domain(domain_name, filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Markdown file not found: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    endpoints = []
    categories_map = {}
    current_ep = None
    current_category = "General"

    header_re = re.compile(r'^###\s+([\d\.]+)\s+(.*)$')
    endpoint_re = re.compile(r'^\*\*Endpoint:\*\*\s+`([A-Z]+)\s+([^`]+)`')
    scopes_re = re.compile(r'^\*\*Required Scopes:\*\*\s+`(.*)`$')
    cat_re = re.compile(r'^##\s+[\d\.]+\s+(.*)$')

    for idx, line in enumerate(lines, 1):
        m_cat = cat_re.match(line.strip())
        if m_cat:
            current_category = m_cat.group(1).strip()
            if current_category not in categories_map:
                slug = re.sub(r'[^a-z0-9-]+', '', current_category.lower().replace(' ', '-'))
                categories_map[current_category] = slug
            continue

        m_hdr = header_re.match(line.strip())
        if m_hdr:
            if current_ep:
                current_ep['end_line'] = idx - 1
                endpoints.append(current_ep)
            current_ep = {
                'domain_name': domain_name,
                'category_name': current_category,
                'section_number': m_hdr.group(1).strip(),
                'title': m_hdr.group(2).strip(),
                'method': '',
                'path': '',
                'summary': [],
                'required_scopes': '',
                'filepath': filepath,
                'start_line': idx,
                'end_line': idx
            }
            continue

        if current_ep:
            m_ep = endpoint_re.match(line.strip())
            if m_ep:
                current_ep['method'] = m_ep.group(1).strip()
                current_ep['path'] = m_ep.group(2).strip()
                continue
            m_sc = scopes_re.match(line.strip())
            if m_sc:
                current_ep['required_scopes'] = m_sc.group(1).strip()
                continue
            if not line.startswith('#') and not line.startswith('```') and not line.startswith('|') and not line.startswith('- **`') and line.strip():
                if len(current_ep['summary']) < 3:
                    current_ep['summary'].append(line.strip())

    if current_ep:
        current_ep['end_line'] = len(lines)
        endpoints.append(current_ep)

    for ep in endpoints:
        ep['summary'] = " ".join(ep['summary'])

    return categories_map, endpoints


def index_domain_in_db(domain_name, filepath, db_path=None):
    if not db_path:
        db_path = get_default_db_path()

    init_db(db_path)
    session = get_session()

    # Get or create Domain
    domain = session.query(Domain).filter_by(name=domain_name).first()
    if not domain:
        domain = Domain(name=domain_name, title=f"Webex {domain_name.capitalize()}")
        session.add(domain)
        session.commit()

    categories_map, endpoints_data = parse_md_for_domain(domain_name, filepath)

    # Clear existing categories and endpoints for this domain
    session.query(Endpoint).filter_by(domain_id=domain.id).delete()
    session.query(Category).filter_by(domain_id=domain.id).delete()
    session.commit()

    cat_objects = {}
    for cat_name, slug in categories_map.items():
        cat = Category(domain_id=domain.id, name=cat_name, slug=slug)
        session.add(cat)
        session.commit()
        cat_objects[cat_name] = cat.id

    for ep in endpoints_data:
        cat_id = cat_objects.get(ep['category_name'])
        if not cat_id:
            # fallback category
            cat = Category(domain_id=domain.id, name=ep['category_name'], slug="general")
            session.add(cat)
            session.commit()
            cat_id = cat.id
            cat_objects[ep['category_name']] = cat.id

        endpoint = Endpoint(
            domain_id=domain.id,
            category_id=cat_id,
            section_number=ep['section_number'],
            title=ep['title'],
            method=ep['method'],
            path=ep['path'],
            summary=ep['summary'],
            required_scopes=ep['required_scopes'],
            doc_filepath=ep['filepath'],
            start_line=ep['start_line'],
            end_line=ep['end_line']
        )
        session.add(endpoint)

    domain.total_endpoints = len(endpoints_data)
    session.commit()
    session.close()

    # Rebuild FTS5 table
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DELETE FROM endpoints_fts WHERE domain_name = ?", (domain_name,))
    for ep in endpoints_data:
        cur.execute('''
        INSERT INTO endpoints_fts (domain_name, category_name, title, method, path, summary)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            domain_name,
            ep['category_name'],
            ep['title'],
            ep['method'],
            ep['path'],
            ep['summary']
        ))
    conn.commit()
    conn.close()

    return len(endpoints_data), len(categories_map)
