---
title: Hermes Output
layout: default
---

<style>
  :root { color-scheme: dark; }
  body { background: #0d1117; color: #e6edf3; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
  .container-lg { max-width: 900px; margin: 0 auto; padding: 32px 16px; }
  h1 { border-bottom: 1px solid #30363d; padding-bottom: 8px; font-weight: 600; }
  h2 { margin-top: 32px; font-weight: 600; }
  a { color: #58a6ff; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .file-grid { display: flex; flex-direction: column; gap: 4px; }
  .file-item { padding: 8px 12px; background: #161b22; border: 1px solid #30363d; border-radius: 6px; display: flex; align-items: center; gap: 8px; }
  .file-item:hover { background: #1c2128; }
  .file-icon { font-size: 18px; min-width: 24px; text-align: center; }
  .file-name { flex: 1; }
  .file-meta { color: #8b949e; font-size: 12px; }
  .tag { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 500; }
  .tag-blue { background: #1f6feb33; color: #58a6ff; border: 1px solid #1f6feb66; }
  .tag-green { background: #23863633; color: #3fb950; border: 1px solid #23863666; }
  .tag-purple { background: #8957e533; color: #a371f7; border: 1px solid #8957e566; }
  .tag-orange { background: #d2992233; color: #d29922; border: 1px solid #d2992266; }
  .hero { text-align: center; padding: 48px 0 32px; }
  .hero h1 { border: none; font-size: 32px; }
  .hero p { color: #8b949e; font-size: 16px; max-width: 500px; margin: 0 auto; }
  .section-title { margin-top: 40px; margin-bottom: 12px; }
  .feed { margin-top: 24px; padding: 0; list-style: none; }
  .feed li { padding: 6px 0; border-bottom: 1px solid #21262d; font-size: 14px; }
  .feed time { color: #8b949e; margin-right: 8px; }
</style>

<div class="hero">
  <h1>⎇ Hermes Output</h1>
  <p>Daily sync of generated dashboards, briefs, and visual reports from the Hermes agent</p>
  <div style="margin-top: 16px;">
    <span class="tag tag-blue">auto-sync</span>
    <span class="tag tag-green">daily</span>
    <span class="tag tag-purple">dark-mode</span>
  </div>
</div>

## 📁 Directories

{% assign dirs = site.static_files | where_exp: "file", "file.path contains '/briefs/' or file.path contains '/business-ops/'" | group_by_exp: "file", "file.path | split: '/' | slice: 0, 3 | join: '/'" %}
{% for dir in dirs %}
  {% assign parts = dir.name | split: '/' %}
  {% if parts.size == 3 and parts[2] != "" %}
    {% assign dir_name = parts[2] %}
    {% assign dir_path = dir.name | append: '/' %}
    {% assign file_count = dir.items | size %}
    <div class="file-item">
      <span class="file-icon">📂</span>
      <span class="file-name"><a href="{{ site.baseurl }}/{{ dir_path | relative_url }}">{{ dir_name | capitalize | replace: "-", " " }}</a></span>
      <span class="file-meta">{{ file_count }} files</span>
    </div>
  {% endif %}
{% endfor %}

## 📄 Recent Files

<div class="file-grid">
{% assign sorted = site.static_files | sort: "modified_time" | reverse %}
{% for file in sorted limit: 20 %}
  {% assign ext = file.path | split: '.' | last | downcase %}
  {% if ext == "html" or ext == "md" or ext == "excalidraw" or ext == "json" %}
    {% if file.path contains "hermes-output" %}
      <div class="file-item">
        <span class="file-icon">
          {% if ext == "html" %}🌐{% elsif ext == "md" %}📝{% elsif ext == "excalidraw" %}🎨{% else %}📄{% endif %}
        </span>
        <span class="file-name"><a href="{{ site.baseurl }}{{ file.path | relative_url }}">{{ file.name | replace: "-", " " | replace: ".md", "" | replace: ".html", "" }}</a></span>
        <span class="file-meta">.{{ ext }}</span>
      </div>
    {% endif %}
  {% endif %}
{% endfor %}
</div>

---

<p style="text-align: center; color: #8b949e; font-size: 12px; margin-top: 48px;">
  Last synced: {{ site.time | date: "%Y-%m-%d %H:%M UTC" }} · 
  <a href="https://github.com/Jason-md-byte/hermes-pages">Source repo</a>
</p>
