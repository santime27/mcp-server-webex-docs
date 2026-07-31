import os
import json
import re

def build_markdown_for_domain(domain_name, root_node, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{domain_name}.md")

    md_lines = []
    title = root_node.get('title', f"Webex {domain_name.capitalize()}: All APIs")
    md_lines.append(f"# {title} Documentation & Schema Reference")
    md_lines.append("")
    md_lines.append(f"This document is an automated structured reference of all API endpoints under **{title}**, including OpenAPI specifications, HTTP methods, paths, parameters, request body schemas, and response schemas.")
    md_lines.append("")
    md_lines.append("## Table of Contents")
    md_lines.append("")

    categories = root_node.get('subMenu', [])
    for i, cat in enumerate(categories, 1):
        cat_title = cat.get('title', '').replace('All APIs: ', '').strip()
        slug = re.sub(r'[^a-z0-9-]+', '', cat_title.lower().replace(' ', '-').replace('/', '-').replace(':', '-'))
        md_lines.append(f"- [{i}. {cat_title}](#{i}-{slug})")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")

    total_eps = 0

    def format_endpoint(ep, sec_num):
        lines = []
        ep_title = ep.get('title', '')
        url = ep.get('url', '')
        spec_wrap = ep.get('versions', [{}])[0].get('spec', '{}')
        try:
            spec_obj = json.loads(spec_wrap)
            inner = spec_obj.get('spec', {})
            if isinstance(inner, str):
                inner = json.loads(inner)
        except Exception:
            inner = {}
        
        method = inner.get('method', ep.get('type', '')).upper()
        path = inner.get('path', url)
        desc = inner.get('description', '') or inner.get('summary', '')
        
        lines.append(f"### {sec_num} {ep_title}")
        lines.append("")
        lines.append(f"**Endpoint:** `{method} {path}`")
        lines.append("")
        if desc:
            lines.append(desc.strip())
            lines.append("")
            
        # Security / Scopes
        sec = inner.get('security', [])
        if sec:
            scopes = []
            for s in sec:
                if isinstance(s, dict):
                    for k, v in s.items():
                        if isinstance(v, list):
                            scopes.extend(v)
                        else:
                            scopes.append(str(v))
            if scopes:
                lines.append("**Required Scopes:** `" + "`, `".join(sorted(list(set(scopes)))) + "`")
                lines.append("")
                
        # Parameters
        params = inner.get('parameters', [])
        if params:
            lines.append("#### Parameters")
            lines.append("")
            lines.append("| Name | In | Type | Required | Description |")
            lines.append("| :--- | :--- | :--- | :--- | :--- |")
            for p in params:
                name = str(p.get('name', ''))
                in_loc = str(p.get('in', ''))
                schema = p.get('schema', {})
                p_type = str(schema.get('type', p.get('type', 'string')))
                req = 'Yes' if p.get('required') else 'No'
                p_desc = str(p.get('description', '')).replace('\n', ' ').replace('|', '&#124;')
                lines.append(f"| `{name}` | `{in_loc}` | `{p_type}` | {req} | {p_desc} |")
            lines.append("")
            
        # Request Body
        rb = inner.get('requestBody', {})
        if rb:
            lines.append("#### Request Body Schema")
            lines.append("")
            desc_rb = rb.get('description', '')
            if desc_rb:
                lines.append(desc_rb)
                lines.append("")
            content = rb.get('content', {})
            json_content = content.get('application/json', content.get('application/json-patch+json', {}))
            schema = json_content.get('schema', {})
            if schema:
                lines.append("```json")
                lines.append(json.dumps(schema, indent=2))
                lines.append("```")
                lines.append("")
                
        # Responses
        responses = inner.get('responses', {})
        if responses:
            lines.append("#### Responses")
            lines.append("")
            for code, resp in responses.items():
                r_desc = resp.get('description', '')
                lines.append(f"- **`{code}`** — {r_desc}")
                content = resp.get('content', {}).get('application/json', {})
                schema = content.get('schema', {})
                if schema:
                    lines.append("  ```json")
                    schema_str = json.dumps(schema, indent=2)
                    for l in schema_str.splitlines():
                        lines.append("  " + l)
                    lines.append("  ```")
            lines.append("")
            
        lines.append("---")
        lines.append("")
        return lines

    for i, cat in enumerate(categories, 1):
        cat_title = cat.get('title', '').replace('All APIs: ', '').strip()
        md_lines.append(f"## {i}. {cat_title}")
        md_lines.append("")
        
        def process_node(node, prefix):
            nonlocal total_eps
            if not node.get('subMenu'):
                total_eps += 1
                md_lines.extend(format_endpoint(node, prefix))
            else:
                for j, child in enumerate(node.get('subMenu', []), 1):
                    process_node(child, f"{prefix}.{j}")
                    
        for j, child in enumerate(cat.get('subMenu', []), 1):
            process_node(child, f"{i}.{j}")

    out_text = "\n".join(md_lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(out_text)

    return output_path, total_eps, len(categories)
