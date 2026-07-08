#!/usr/bin/env python3
"""Weekly link check for provider URLs.

For each provider, sends a lightweight GET to its URL. If reachable (HTTP 2xx),
updates `last_checked` to today. Providers that fail are flagged but kept.
Writes back to data/providers.json.
"""
import datetime as dt
import json
import os
import urllib.request
import urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "providers.json")
TODAY = dt.datetime.now(dt.timezone.utc).date().isoformat()


def check(url):
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "free-ai-api-tiers-bot"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status < 400
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError):
        return False


def main():
    with open(DATA) as f:
        data = json.load(f)
    changed = False
    for p in data["providers"]:
        ok = check(p["url"])
        status = "ok" if ok else "UNREACHABLE"
        if ok:
            if p.get("last_checked") != TODAY:
                p["last_checked"] = TODAY
                changed = True
        else:
            print(f"  [WARN] {p['name']} -> {status}: {p['url']}")
        print(f"  {status:12} {p['name']}")
    with open(DATA, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("link check done." if changed else "link check done (no date changes).")


if __name__ == "__main__":
    main()
