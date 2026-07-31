import os
import sys
import sqlite3
import logging
from typing import Optional, List, Dict, Any

# Ensure project root is in sys.path so 'python3 /path/to/src/server.py' works anywhere without PYTHONPATH
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("webex-api-docs-mcp")

from mcp.server.fastmcp import FastMCP
from src.models.db import Domain, Category, Endpoint, get_session, get_default_db_path

mcp = FastMCP("webex-api-docs-mcp")

@mcp.tool()
def list_webex_domains() -> List[Dict[str, Any]]:
    """List all available Webex API documentation domains (e.g. admin, calling, meetings, messaging) and their endpoint counts.
    """
    logger.info("Executing tool: list_webex_domains")
    session = get_session()
    domains = session.query(Domain).all()
    res = [
        {
            "name": d.name,
            "title": d.title,
            "total_endpoints": d.total_endpoints
        }
        for d in domains
    ]
    session.close()
    return res


@mcp.tool()
def list_webex_categories(domain: str) -> List[Dict[str, Any]]:
    """List all API categories available within a specific Webex domain (admin, calling, meetings, or messaging).
    
    Args:
        domain: The name of the domain (e.g., 'admin', 'calling', 'meetings', 'messaging')
    """
    logger.info("Executing tool: list_webex_categories for domain='%s'", domain)
    session = get_session()
    d = session.query(Domain).filter_by(name=domain.lower()).first()
    if not d:
        session.close()
        return [{"error": f"Domain '{domain}' not found."}]

    cats = session.query(Category).filter_by(domain_id=d.id).all()
    res = [
        {
            "category_name": c.name,
            "slug": c.slug
        }
        for c in cats
    ]
    session.close()
    return res


@mcp.tool()
def search_webex_api_docs(
    query: str,
    domain: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = 15
) -> List[Dict[str, Any]]:
    """Search Webex API documentation across all 1,400+ endpoints using local SQLite FTS5 full-text search.
    
    Args:
        query: Keyword or phrase to search for (e.g., 'audit events', 'create user', 'call queue', 'recordings')
        domain: Optional domain filter ('admin', 'calling', 'meetings', or 'messaging')
        category: Optional category filter (e.g., 'Admin Audit Events', 'Call Routing')
        limit: Max number of results to return (default 15)
    """
    logger.info("Executing tool: search_webex_api_docs with query='%s', domain='%s', category='%s'", query, domain, category)
    db_path = get_default_db_path()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    sql = "SELECT e.*, d.name as domain_name, c.name as category_name FROM endpoints e JOIN domains d ON e.domain_id = d.id JOIN categories c ON e.category_id = c.id"
    conditions = []
    params = []

    if query:
        sql = "SELECT e.*, d.name as domain_name, c.name as category_name FROM endpoints e JOIN domains d ON e.domain_id = d.id JOIN categories c ON e.category_id = c.id JOIN endpoints_fts fts ON e.id = fts.rowid"
        conditions.append("endpoints_fts MATCH ?")
        words = query.strip().split()
        fts_query = " OR ".join(f"{w}*" for w in words)
        params.append(fts_query)

    if domain:
        conditions.append("d.name = ?")
        params.append(domain.lower())

    if category:
        conditions.append("c.name LIKE ?")
        params.append(f"%{category}%")

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    sql += " LIMIT ?"
    params.append(limit)

    rows = cur.execute(sql, params).fetchall()
    results = []
    for r in rows:
        results.append({
            "domain": r["domain_name"],
            "section_number": r["section_number"],
            "title": r["title"],
            "category": r["category_name"],
            "method": r["method"],
            "path": r["path"],
            "summary": r["summary"][:200] if r["summary"] else "",
            "start_line": r["start_line"],
            "end_line": r["end_line"],
            "doc_filepath": r["doc_filepath"]
        })

    conn.close()
    return results


@mcp.tool()
def get_webex_endpoint_schema(domain: str, section_number: str) -> Dict[str, Any]:
    """Retrieve the complete OpenAPI documentation block, parameters table, and JSON schemas for a specific Webex API endpoint.
    
    Args:
        domain: Domain name ('admin', 'calling', 'meetings', or 'messaging')
        section_number: Section number of the endpoint (e.g., '1.1', '2.5', '5.10')
    """
    logger.info("Executing tool: get_webex_endpoint_schema for domain='%s', section='%s'", domain, section_number)
    session = get_session()
    d = session.query(Domain).filter_by(name=domain.lower()).first()
    if not d:
        session.close()
        return {"error": f"Domain '{domain}' not found."}

    ep = session.query(Endpoint).filter_by(domain_id=d.id, section_number=section_number).first()
    if not ep:
        session.close()
        return {"error": f"Endpoint with section '{section_number}' not found in domain '{domain}'."}

    result = {
        "domain": d.name,
        "section_number": ep.section_number,
        "title": ep.title,
        "method": ep.method,
        "path": ep.path,
        "required_scopes": ep.required_scopes,
        "start_line": ep.start_line,
        "end_line": ep.end_line,
        "full_markdown_content": ""
    }

    try:
        with open(ep.doc_filepath, "r", encoding="utf-8") as f:
            all_lines = f.readlines()
            snippet = "".join(all_lines[ep.start_line - 1 : ep.end_line])
            result["full_markdown_content"] = snippet.rstrip()
    except Exception as e:
        result["error"] = f"Error reading markdown file: {str(e)}"

    session.close()
    return result


if __name__ == "__main__":
    logger.info("========================================================================")
    logger.info("Starting webex-api-docs-mcp server - Built by Santiago Meneses Garcia")
    logger.info("Database loaded from: %s", get_default_db_path())
    logger.info("========================================================================")
    mcp.run()
