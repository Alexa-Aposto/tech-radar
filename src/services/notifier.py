"""Threshold-gated email notification — only fires when something important happens."""

import os
import smtplib
import logging
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

from ..models import ContentItem, NotificationConfig

logger = logging.getLogger(__name__)


def send_notification(
    config: NotificationConfig,
    all_items: List[ContentItem],
    date: str,
) -> bool:
    """Send an email with items above notify_threshold. Silent if none qualify.

    Returns True if email was sent, False otherwise.
    """
    email_address = os.getenv(config.email_address_env, "")
    password = os.getenv(config.password_env, "")
    recipients_raw = os.getenv(config.recipients_env, "")
    recipients = [r.strip() for r in recipients_raw.split(",") if r.strip()]

    if not config.enabled or not recipients:
        return False

    if not password or not email_address:
        logger.warning("SMTP email or password env vars not set, skipping notification")
        return False

    hot = [i for i in all_items if (i.ai_score or 0) >= config.notify_threshold]
    if not hot:
        logger.info("No items above notify threshold — staying silent")
        return False

    rest_count = len(all_items) - len(hot)

    # --- plain text ---
    text_lines = [f"☀️ Tech Radar — {date}", ""]
    for item in hot:
        text_lines.append(item.title)
        note = item.metadata.get("relevance") or item.ai_reason or ""
        if note:
            text_lines.append(f"→ {note}")
        text_lines.append(str(item.url))
        text_lines.append("")

    text_lines.append("—")
    if rest_count > 0:
        text_lines.append(f"Also: {rest_count} other items in the full briefing")
    if config.pages_url:
        text_lines.append(config.pages_url)

    text_body = "\n".join(text_lines)

    # --- html ---
    items_html = ""
    for item in hot:
        note = item.metadata.get("relevance") or item.ai_reason or ""
        note_html = (
            f'<div style="color:#555;font-size:13px;margin-top:2px">→ {note}</div>'
            if note else ""
        )
        items_html += f"""
        <div style="margin-bottom:20px">
            <a href="{item.url}" style="color:#2563eb;text-decoration:none;font-size:15px;font-weight:600">{item.title}</a>
            {note_html}
        </div>"""

    footer_parts = []
    if rest_count > 0:
        footer_parts.append(f"Also: {rest_count} other items in the full briefing")
    if config.pages_url:
        footer_parts.append(
            f'<a href="{config.pages_url}" style="color:#2563eb">📖 Full briefing</a>'
        )
    footer_html = "<br>".join(footer_parts)

    html_body = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"></head>
<body style="font-family:-apple-system,BlinkMacSystemFont,sans-serif;max-width:560px;margin:0 auto;padding:20px;color:#1a1a1a">
<h2 style="margin:0 0 20px;font-weight:600">☀️ Tech Radar — {date}</h2>
{items_html}
<div style="border-top:1px solid #e5e5e5;padding-top:12px;margin-top:8px;color:#888;font-size:13px">
{footer_html}
</div>
</body></html>"""

    subject = f"☀️ Tech Radar — {date}"

    try:
        with smtplib.SMTP_SSL(config.smtp_server, config.smtp_port) as server:
            server.login(email_address, password)
            for recipient in recipients:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = Header(subject, "utf-8")
                msg["From"] = f"Horizon <{email_address}>"
                msg["To"] = recipient
                msg.attach(MIMEText(text_body, "plain", "utf-8"))
                msg.attach(MIMEText(html_body, "html", "utf-8"))
                server.send_message(msg)
                logger.info(f"Notification sent to {recipient}")
        return True
    except Exception as e:
        logger.error(f"Notification failed: {e}")
        return False
