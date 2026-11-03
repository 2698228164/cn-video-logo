#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描 icon/*.png 生成 Logo.json（与 Rex/Logo.json 同结构）
URL 基址优先取环境变量 LOGO_BASE，其次 GITHUB_REPOSITORY+main，方便本地/CI 通用。
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ICON_DIR = os.path.join(ROOT, "icon")
META_PATH = os.path.join(ROOT, "_meta.json")
OUT_PATH = os.path.join(ROOT, "Logo.json")

META = json.load(open(META_PATH, encoding="utf-8")) if os.path.exists(META_PATH) else {"cn": {}, "en": {}}


def base_url():
    if os.environ.get("LOGO_BASE"):
        return os.environ["LOGO_BASE"].rstrip("/") + "/"
    repo = os.environ.get("GITHUB_REPOSITORY", "YOUR_NAME/cn-video-logo")
    return f"https://raw.githubusercontent.com/{repo}/main/"


def main():
    base = base_url()
    icons = []
    for fn in sorted(os.listdir(ICON_DIR)):
        if not fn.lower().endswith(".png"):
            continue
        name = os.path.splitext(fn)[0]
        icons.append({
            "name": name,
            "label": META.get("cn", {}).get(name, name),
            "url": base + "icon/" + fn,
        })
    data = {
        "name": "CN_Video_Logo",
        "description": "国内主流视频平台图标集",
        "icons": icons,
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"wrote {OUT_PATH} ({len(icons)} icons, base={base})")

    state = os.environ.get("GITHUB_STATE")
    if state:
        with open(state, "a", encoding="utf-8") as f:
            f.write(f"LOGO_JSON_PATH={OUT_PATH}\n")


if __name__ == "__main__":
    main()
