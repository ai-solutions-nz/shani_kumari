#!/usr/bin/env python3
"""Read-only WordPress content and media export for the Shani React migration.

Run in a network-enabled environment (Bolt terminal or GitHub Actions):
    python3 scripts/export_wordpress.py

Writes content snapshots and referenced original media under public/wp-migration/.
Does not change WordPress or publish a website.
"""
import json
import mimetypes
import os
from pathlib import Path
import re
import time
from urllib.parse import urlparse
from urllib.request import Request, urlopen

SITE = "https://shanikumari.co.nz"
DEST = Path("public/wp-migration")
API = SITE + "/wp-json/wp/v2"
MAX_BYTES = 60 * 1024 * 1024
HEADERS = {"User-Agent": "ShaniKumariMigration/1.0 (authorized site migration)"}


def fetch(url):
    req = Request(url, headers=HEADERS)
    for attempt in range(3):
        try:
            with urlopen(req, timeout=35) as resp:
                data = resp.read(MAX_BYTES + 1)
                if len(data) > MAX_BYTES:
                    raise RuntimeError("Asset exceeds 60 MB: " + url)
                return data
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))


def list_endpoint(name):
    results = []
    page = 1
    while True:
        url = f"{API}/{name}?per_page=100&page={page}&_embed"
        try:
            batch = json.loads(fetch(url))
        except Exception as exc:
            if page > 1 and "404" in str(exc):
                break
            raise
        if not isinstance(batch, list):
            raise RuntimeError("Unexpected WordPress API response for " + name)
        results.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return results


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    manifest = {"source": SITE, "pages": 0, "posts": 0, "media": 0, "downloaded": 0, "failed_media": []}
    for kind in ("pages", "posts"):
        items = list_endpoint(kind)
        # Preserve original published content, slug, metadata and source URL for review.
        records = [{
            "id": item.get("id"),
            "slug": item.get("slug"),
            "link": item.get("link"),
            "modified": item.get("modified"),
            "title": item.get("title", {}).get("rendered", ""),
            "content": item.get("content", {}).get("rendered", ""),
            "excerpt": item.get("excerpt", {}).get("rendered", ""),
            "featured_media": item.get("featured_media"),
            "status": item.get("status"),
            "yoast_head_json": item.get("yoast_head_json"),
        } for item in items if item.get("status") == "publish"]
        write_json(DEST / (kind + ".json"), records)
        manifest[kind] = len(records)

    media = list_endpoint("media")
    records = []
    for item in media:
        url = item.get("source_url", "")
        if not url:
            continue
        parsed = urlparse(url)
        # Only download assets served by the authorized source host.
        if parsed.hostname != "shanikumari.co.nz":
            continue
        original = parsed.path.rsplit("/", 1)[-1]
        safe = re.sub(r"[^A-Za-z0-9._-]", "_", original)
        path = DEST / "media" / str(item["id"]) / safe
        record = {"id": item["id"], "source_url": url, "local_path": "/" + str(path).replace(os.sep, "/"), "mime_type": item.get("mime_type"), "alt_text": item.get("alt_text", ""), "title": item.get("title", {}).get("rendered", "")}
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            if not path.exists() or path.stat().st_size == 0:
                data = fetch(url)
                path.write_bytes(data)
            record["size"] = path.stat().st_size
            manifest["downloaded"] += 1
        except Exception as exc:
            record["error"] = str(exc)
            manifest["failed_media"].append({"id": item["id"], "url": url, "error": str(exc)})
        records.append(record)
    write_json(DEST / "media.json", records)
    manifest["media"] = len(records)
    write_json(DEST / "export-manifest.json", manifest)
    print(json.dumps(manifest, indent=2))
    if manifest["failed_media"]:
        raise SystemExit("Some media downloads failed; see export-manifest.json")


if __name__ == "__main__":
    main()
