import os
import sys
from src.pipeline.fetcher import DOMAIN_CONFIGS, fetch_domain_data
from src.pipeline.markdown_builder import build_markdown_for_domain
from src.pipeline.roomos_builder import build_roomos_markdown
from src.pipeline.db_indexer import index_domain_in_db
from src.models.db import init_db, get_default_db_path

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_dir = os.path.join(base_dir, 'data')
    docs_dir = os.path.join(base_dir, 'docs')
    db_path = get_default_db_path()

    print("=== STARTING WEBEX API DOCS MCP PIPELINE (ETL) ===")
    print(f"Docs Directory: {docs_dir}")
    print(f"Database Path:  {db_path}")
    print("-" * 70)

    init_db(db_path)

    total_all_endpoints = 0
    results = []

    for domain_name in ['admin', 'calling', 'meetings', 'messaging', 'roomos']:
        print(f"Processing domain: '{domain_name.upper()}' ...")
        try:
            if domain_name == 'roomos':
                md_path, total_eps, total_cats = build_roomos_markdown(data_dir, docs_dir)
            else:
                root_node = fetch_domain_data(domain_name)
                md_path, total_eps, total_cats = build_markdown_for_domain(domain_name, root_node, docs_dir)
            
            eps_indexed, cats_indexed = index_domain_in_db(domain_name, md_path, db_path)
            
            results.append({
                'domain': domain_name,
                'categories': cats_indexed,
                'endpoints': eps_indexed,
                'md_path': md_path
            })
            total_all_endpoints += eps_indexed
            print(f"  -> Generated {md_path} ({eps_indexed} endpoints)")
            print(f"  -> Indexed into SQLite FTS5 ({eps_indexed} endpoints, {cats_indexed} categories)")
        except Exception as e:
            print(f"  [ERROR] Processing {domain_name} failed: {e}")
        print("-" * 70)

    print("=== PIPELINE COMPLETION SUMMARY ===")
    print(f"{'DOMAIN':<12} | {'CATEGORIES':<12} | {'ENDPOINTS':<12} | {'FILE':<30}")
    print("-" * 70)
    for res in results:
        print(f"{res['domain'].upper():<12} | {res['categories']:<12} | {res['endpoints']:<12} | {os.path.basename(res['md_path']):<30}")
    print("-" * 70)
    print(f"TOTAL ENDPOINTS INDEXED: {total_all_endpoints}")
    print(f"SQLAlchemy SQLite DB ready at: {db_path}")

if __name__ == '__main__':
    main()
