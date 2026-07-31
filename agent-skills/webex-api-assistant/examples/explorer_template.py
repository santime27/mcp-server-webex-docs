#!/usr/bin/env python3
"""
Webex API Exploration Reference Template
----------------------------------------
This template demonstrates best practices for exploring Webex APIs in a temporary/sandbox script:
- Reads access token from environment variables (NEVER hardcodes tokens).
- Sets correct standard HTTP headers.
- Handles common Webex API error codes (401, 403, 404, 429 rate limits, 500).
- Pretty-prints JSON responses for easy inspection.
"""

import os
import sys
import json
import time
import requests
from typing import Optional, Dict, Any

WEBEX_BASE_URL = "https://webexapis.com/v1"


def get_access_token() -> str:
    """Retrieve Webex token from environment variable."""
    token = os.getenv("WEBEX_ACCESS_TOKEN") or os.getenv("WEBEX_TOKEN")
    if not token:
        print("[ERROR] No Webex access token detected in environment.")
        print("Please export your token before running this script:")
        print("    export WEBEX_ACCESS_TOKEN='your_personal_access_token_or_oauth_token'")
        sys.exit(1)
    return token


def make_webex_request(
    method: str,
    endpoint_path: str,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    timeout: int = 15
) -> Optional[Dict[str, Any]]:
    """Execute an HTTP request to Webex REST API with rate-limit retry and error handling."""
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    url = endpoint_path if endpoint_path.startswith("http") else f"{WEBEX_BASE_URL}/{endpoint_path.lstrip('/')}"
    print(f"[INFO] {method.upper()} {url}")

    if params:
        print(f"[INFO] Query Params: {json.dumps(params)}")
    if json_body:
        print(f"[INFO] Request Body: {json.dumps(json_body)}")

    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            json=json_body,
            timeout=timeout
        )

        # Handle 429 Too Many Requests (Rate Limiting)
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 15))
            print(f"[WARNING] Rate limit reached (429). Retrying after {retry_after} seconds...")
            time.sleep(retry_after)
            return make_webex_request(method, endpoint_path, params, json_body, timeout)

        response.raise_for_status()

        # Handle 204 No Content
        if response.status_code == 204 or not response.content:
            print("[SUCCESS] Operation successful (204 No Content).")
            return None

        return response.json()

    except requests.exceptions.HTTPError as e:
        status = e.response.status_code
        print(f"[HTTP ERROR] Status Code: {status}")
        print(f"[HTTP ERROR] Response Body: {e.response.text}")
        if status == 401:
            print("[HINT] Token may be expired or invalid. Check developer.webex.com.")
        elif status == 403:
            print("[HINT] Token lacks required OAuth scope for this endpoint or user lacks admin permissions.")
        elif status == 404:
            print("[HINT] Resource ID or endpoint URL path not found.")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected error: {str(e)}")
        return None


def main():
    # Example exploration: Get current user profile (/people/me)
    print("=========================================================")
    print("Starting Webex API Exploration - /v1/people/me")
    print("=========================================================")

    result = make_webex_request("GET", "/people/me")
    if result:
        print("\n[SUCCESS] Response Data:")
        print(json.dumps(result, indent=2))
        print("=========================================================")


if __name__ == "__main__":
    main()
