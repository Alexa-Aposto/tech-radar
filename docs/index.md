---
layout: default
title: Home
---

# Tech Radar

AI-curated intelligence briefing for AI-powered K8s platforms and NLP research.

Runs twice a week — Monday morning and Friday evening.

## Briefings

<ul>
  {% assign en_posts = site.posts | where: "lang", "en" %}
  {% for post in en_posts limit:20 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a>
    </li>
  {% else %}
    <li><em>No briefings yet</em></li>
  {% endfor %}
</ul>
