# CN Video Logo

国内主流视频平台图标集，结构与 [Rex/Logo.json](../../) 一致：一个 `Logo.json` 清单 + `icon/` 下的 PNG。

- `Logo.json` 由 GitHub Actions 自动生成，**不要手改**。
- 新增平台：把 1024×1024 PNG 丢进 `icon/`，命名 `序号_英文名.png`（如 `017_xxx.png`），push 即可。
- 生成脚本：`.github/scripts/generate_logo_json.py`

## 客户端用法

```
GET https://raw.githubusercontent.com/<你的用户名>/cn-video-logo/main/Logo.json
```

遍历 `icons`，按 `url` 异步加载并缓存（key 用 `name`）；`label` 是中文字段，省去客户端再维护一份中文名。

## 本地预览

```sh
python3 -m http.server 8080
# 打开 http://localhost:8080/
```

## 素材来源

- 品牌词标：中文/英文维基百科（SVG 渲染 1024px，透明背景）
- 商店图标：Apple App Store 官方 1024px 图标

图标版权归各平台所有，仅用于标识，商用请先确认授权。
