#!/usr/bin/env python3
"""
RoomOS xAPI Documentation Builder
---------------------------------
Fetches the official Cisco RoomOS xAPI schema (from cisco-ce/roomos.cisco.com repository),
generates a comprehensive Markdown reference doc (docs/roomos.md) complete with usage
syntax (REST API, CLI/Macro, JSXAPI), parameters tables, and scopes, and prepares it for
SQLAlchemy + SQLite FTS5 indexing.
"""

import os
import json
import re
import urllib.request
from typing import Dict, Any, List, Tuple

ROOMOS_SCHEMA_URL = "https://raw.githubusercontent.com/cisco-ce/roomos.cisco.com/master/schemas/26.7.1%20June%202026.json"
CACHE_FILENAME = "roomos_schema.json"


def get_schema_data(data_dir: str) -> Dict[str, Any]:
    """Retrieve RoomOS schema JSON from cache or download from official GitHub repository."""
    os.makedirs(data_dir, exist_ok=True)
    cache_path = os.path.join(data_dir, CACHE_FILENAME)

    if os.path.exists(cache_path):
        print(f"[INFO] Using cached RoomOS schema at {cache_path}")
        with open(cache_path, "r", encoding="utf-8") as f:
            return json.load(f)

    print(f"[INFO] Downloading official RoomOS schema from {ROOMOS_SCHEMA_URL} ...")
    req = urllib.request.Request(
        ROOMOS_SCHEMA_URL,
        headers={"User-Agent": "Mozilla/5.0 (compatible; WebexDocsETL/1.0)"}
    )
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode("utf-8"))
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(data, f)
        print(f"[INFO] Saved RoomOS schema cache ({len(data.get('objects', []))} objects) to {cache_path}")
        return data


def format_valuespace(vs: Dict[str, Any]) -> str:
    """Format parameter valuespace (range or enum values) into readable Markdown."""
    if not vs:
        return "-"
    v_type = vs.get("type", "")
    if "Min" in vs and "Max" in vs:
        return f"{vs['Min']} to {vs['Max']} (`{v_type}`)"
    if "Value" in vs and isinstance(vs["Value"], list):
        vals = [str(x.get("name", x)) if isinstance(x, dict) else str(x) for x in vs["Value"]]
        return ", ".join(f"`{v}`" for v in vals[:15]) + ("..." if len(vals) > 15 else "")
    return str(v_type) or "-"


def build_roomos_markdown(data_dir: str, docs_dir: str) -> Tuple[str, int, int]:
    """Build docs/roomos.md from RoomOS xAPI schema objects."""
    schema = get_schema_data(data_dir)
    objects: List[Dict[str, Any]] = schema.get("objects", [])

    # Group objects by Type
    categories_order = ["Command", "Configuration", "Status", "Event"]
    grouped: Dict[str, List[Dict[str, Any]]] = {cat: [] for cat in categories_order}
    for obj in objects:
        t = obj.get("type", "Command")
        if t in grouped:
            grouped[t].append(obj)
        else:
            grouped.setdefault(t, []).append(obj)

    # Sort each category by path
    for t in grouped:
        grouped[t].sort(key=lambda x: x.get("path", ""))

    os.makedirs(docs_dir, exist_ok=True)
    output_path = os.path.join(docs_dir, "roomos.md")

    lines = []
    lines.append("# Webex RoomOS xAPI: Commands, Configurations, Statuses & Events Reference")
    lines.append("")
    lines.append("This document is the authoritative developer reference for Cisco RoomOS Collaboration Devices (Room Kit, Room Bar, Board Pro, Desk Pro, Codec EQ, etc.), detailing all xAPI Commands, Configurations, Statuses, and Events.")
    lines.append("")

    # --- IN-DEPTH DEVELOPER GUIDE & USAGE METHODS ---
    lines.append("## RoomOS xAPI Developer Guide & Usage Methods")
    lines.append("")
    lines.append("RoomOS devices expose the xAPI hierarchy through multiple interfaces. Below is how to use these APIs across Cloud REST, Node.js JSXAPI, and On-Device CLI/Macros.")
    lines.append("")
    lines.append("#### 1. Webex Cloud REST API (`https://webexapis.com/v1/xapi/`)")
    lines.append("You can execute any RoomOS xCommand or query any xStatus over the Cloud REST API without local network access to the device:")
    lines.append("")
    lines.append("- **Execute a Command (`POST /v1/xapi/command/{commandPath}`)**  ")
    lines.append("  *Required OAuth Scope:* `spark:xapi_commands`  ")
    lines.append("  ```http")
    lines.append("  POST https://webexapis.com/v1/xapi/command/Audio.Volume.Set")
    lines.append("  Authorization: Bearer <WEBEX_ACCESS_TOKEN>")
    lines.append("  Content-Type: application/json")
    lines.append("")
    lines.append("  {")
    lines.append("    \"deviceId\": \"<your_device_id>\",")
    lines.append("    \"arguments\": {")
    lines.append("      \"Level\": 70")
    lines.append("    }")
    lines.append("  }")
    lines.append("  ```")
    lines.append("")
    lines.append("- **Query Device Status (`GET /v1/xapi/status`)**  ")
    lines.append("  *Required OAuth Scope:* `spark:xapi_statuses`  ")
    lines.append("  ```http")
    lines.append("  GET https://webexapis.com/v1/xapi/status?deviceId=<your_device_id>&name=Audio.Volume")
    lines.append("  Authorization: Bearer <WEBEX_ACCESS_TOKEN>")
    lines.append("  ```")
    lines.append("")
    lines.append("#### 2. Node.js JSXAPI Library (`jsxapi`)")
    lines.append("For full-duplex WebSocket or SSH integrations:")
    lines.append("```javascript")
    lines.append("const jsxapi = require('jsxapi');")
    lines.append("const xapi = jsxapi.connect('ssh://admin:password@device.ip');")
    lines.append("")
    lines.append("// Execute Command")
    lines.append("xapi.Command.Audio.Volume.Set({ Level: 70 });")
    lines.append("")
    lines.append("// Query Status")
    lines.append("xapi.Status.Audio.Volume.get().then(volume => console.log('Current volume:', volume));")
    lines.append("")
    lines.append("// Listen to Event / Status changes")
    lines.append("xapi.Status.RoomAnalytics.PeopleCount.Current.on(count => console.log('People in room:', count));")
    lines.append("```")
    lines.append("")
    lines.append("#### 3. CLI / SSH & Macro Syntax (On-Device)")
    lines.append("In the RoomOS device Macro Editor or CLI:")
    lines.append("```bash")
    lines.append("# Execute Command")
    lines.append("xCommand Audio Volume Set Level: 70")
    lines.append("")
    lines.append("# Set Configuration")
    lines.append("xConfiguration Video Input AirPlay Mode: On")
    lines.append("")
    lines.append("# Query Status")
    lines.append("xStatus Audio Volume")
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- TABLE OF CONTENTS ---
    lines.append("## Table of Contents")
    lines.append("")
    for idx, cat_name in enumerate(categories_order, 1):
        lines.append(f"- [{idx}. x{cat_name} ({len(grouped[cat_name])} endpoints)](#{idx}-x{cat_name.lower()})")
    lines.append("")
    lines.append("---")
    lines.append("")

    total_endpoints = 0

    # --- CATEGORY SECTIONS ---
    for cat_idx, cat_name in enumerate(categories_order, 1):
        lines.append(f"## {cat_idx} x{cat_name}")
        lines.append("")

        for ep_idx, obj in enumerate(grouped[cat_name], 1):
            total_endpoints += 1
            path_str = obj.get("path", "")
            dot_path = path_str.replace(" ", ".")
            attrs = obj.get("attributes", {})
            desc = attrs.get("description", "") or f"RoomOS {cat_name}: {path_str}"
            params = attrs.get("params", [])

            sec_num = f"{cat_idx}.{ep_idx}"
            title = f"x{cat_name} {path_str}"

            method_map = {
                "Command": "XCOMMAND",
                "Configuration": "XCONFIG",
                "Status": "XSTATUS",
                "Event": "XEVENT"
            }
            method = method_map.get(cat_name, "XCOMMAND")

            path_prefix_map = {
                "Command": "/v1/xapi/command/",
                "Configuration": "/v1/xapi/status/",
                "Status": "/v1/xapi/status/",
                "Event": "/v1/xapi/event/"
            }
            url_path = path_prefix_map.get(cat_name, "/v1/xapi/") + dot_path

            lines.append(f"### {sec_num} {title}")
            lines.append("")
            lines.append(f"**Endpoint:** `{method} {url_path}`")
            lines.append("")
            if cat_name in ("Command", "Configuration"):
                lines.append("**Required Scopes:** `spark:xapi_commands`, `spark:xapi_statuses`")
            else:
                lines.append("**Required Scopes:** `spark:xapi_statuses`")
            lines.append("")
            if desc:
                lines.append(desc.strip().replace("\r\n", " ").replace("\n", " "))
                lines.append("")

            # Usage syntax snippet
            lines.append("#### Usage Syntax")
            lines.append("")
            if cat_name == "Command":
                lines.append(f"- **REST API (Cloud):** `POST https://webexapis.com/v1/xapi/command/{dot_path}`")
                lines.append(f"- **CLI / Macro:** `xCommand {path_str} [params]`")
                lines.append(f"- **JSXAPI (Node.js):** `xapi.Command.{dot_path}.(...)`")
            elif cat_name == "Configuration":
                lines.append(f"- **CLI / Macro:** `xConfiguration {path_str}: <value>`")
                lines.append(f"- **JSXAPI (Node.js):** `xapi.Config.{dot_path}.set(<value>)`")
            elif cat_name == "Status":
                lines.append(f"- **REST API (Cloud):** `GET https://webexapis.com/v1/xapi/status?deviceId=<id>&name={dot_path}`")
                lines.append(f"- **CLI / Macro:** `xStatus {path_str}`")
                lines.append(f"- **JSXAPI (Node.js):** `xapi.Status.{dot_path}.get()`")
            elif cat_name == "Event":
                lines.append(f"- **JSXAPI (Node.js):** `xapi.Event.{dot_path}.on(event => ...)`")
            lines.append("")

            # Parameters table
            if params:
                lines.append("#### Parameters")
                lines.append("")
                lines.append("| Name | Required | Type | Range / Valuespace | Description |")
                lines.append("| :--- | :--- | :--- | :--- | :--- |")
                for p in params:
                    p_name = str(p.get("name", ""))
                    p_req = "Yes" if p.get("required") else "No"
                    p_vs = p.get("valuespace", {})
                    p_type = str(p_vs.get("type", "String"))
                    p_range = format_valuespace(p_vs)
                    p_desc = str(p.get("description", "")).replace("\r\n", " ").replace("\n", " ").replace("|", "&#124;")
                    lines.append(f"| `{p_name}` | {p_req} | `{p_type}` | {p_range} | {p_desc} |")
                lines.append("")

            # Roles support
            roles = attrs.get("role", [])
            if roles:
                lines.append(f"*Supported Roles:* `{'`, `'.join(roles)}`")
                lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return output_path, total_endpoints, len(categories_order)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_dir = os.path.join(base_dir, "data")
    docs_dir = os.path.join(base_dir, "docs")
    md_path, total_eps, total_cats = build_roomos_markdown(data_dir, docs_dir)
    print(f"[SUCCESS] Built {md_path} with {total_eps} RoomOS xAPI endpoints across {total_cats} categories.")
