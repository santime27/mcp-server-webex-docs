import json
import re
import os

DOMAIN_CONFIGS = {
    'admin': {
        'title': 'Webex Admin: All APIs',
        'url': 'https://developer.webex.com/admin/docs/api',
        'cache_path': '/root/.gemini/antigravity-cli/brain/08329b8f-12b8-41c1-8304-228b450e61ac/.system_generated/steps/3/content.md'
    },
    'calling': {
        'title': 'Webex Cloud Calling: All APIs',
        'url': 'https://developer.webex.com/calling/docs/webex-calling-overview',
        'cache_path': '/root/.gemini/antigravity-cli/brain/08329b8f-12b8-41c1-8304-228b450e61ac/.system_generated/steps/64/content.md'
    },
    'meetings': {
        'title': 'Webex Meetings: All APIs',
        'url': 'https://developer.webex.com/meetings/docs/api',
        'cache_path': '/root/.gemini/antigravity-cli/brain/08329b8f-12b8-41c1-8304-228b450e61ac/.system_generated/steps/143/content.md'
    },
    'messaging': {
        'title': 'Webex Messaging: All APIs',
        'url': 'https://developer.webex.com/messaging/docs/api',
        'cache_path': '/root/.gemini/antigravity-cli/brain/08329b8f-12b8-41c1-8304-228b450e61ac/.system_generated/steps/145/content.md'
    }
}


def extract_initial_state_json(text):
    for line in text.splitlines():
        if 'window.__INITIAL_STATE__ =' in line:
            idx = line.find('window.__INITIAL_STATE__ =')
            json_str = line[idx + len('window.__INITIAL_STATE__ ='):].strip()
            # Replace JavaScript undefined with null
            json_str = re.sub(r'(:\s*)undefined\b', r'\g<1>null', json_str)
            data, _ = json.JSONDecoder().raw_decode(json_str)
            return data
    return None


def find_root_api_node(node, target_titles):
    title = node.get('title', '')
    if any(target in title for target in target_titles):
        return node
    for child in node.get('subMenu', []):
        result = find_root_api_node(child, target_titles)
        if result:
            return result
    return None


def fetch_domain_data(domain_name):
    if domain_name not in DOMAIN_CONFIGS:
        raise ValueError(f"Unknown domain: {domain_name}")

    config = DOMAIN_CONFIGS[domain_name]
    cache_path = config['cache_path']
    if not os.path.exists(cache_path):
        raise FileNotFoundError(f"Cache file not found for {domain_name}: {cache_path}")

    with open(cache_path, 'r', encoding='utf-8') as f:
        text = f.read()

    state = extract_initial_state_json(text)
    if not state:
        raise ValueError(f"Could not extract window.__INITIAL_STATE__ for {domain_name}")

    nav = state.get('sideNavigation', {}).get('sideNavigationData', {})
    root_node = find_root_api_node(nav, [config['title']])
    if not root_node:
        raise ValueError(f"Could not find root API node '{config['title']}' in {domain_name}")

    return root_node
