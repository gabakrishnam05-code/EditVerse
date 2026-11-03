# EDITVERSE — Free + Paid Creative Software Directory

A responsive Flask directory with searchable software cards, category filters, and separate FREE and PAID / PREMIUM sections. Each card opens the vendor's official website in a new tab.

## Run locally on Windows 11 (Python 3.11)
Open CMD inside this folder and run:

```cmd
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. Keep the terminal open while using the local site.

## Publish it free (public URL)
This project includes a `Procfile` for a Python web host such as Render. A typical deployment flow:
1. Create a GitHub account and a new repository.
2. Upload the contents of this project folder to the repository (not the ZIP file itself).
3. Create a free web service on a host that currently offers free Python web services, connect the repository, and use the start command `gunicorn app:app`.
4. After deployment, the host provides a public URL.

Free hosting plans can have limits, sleeping/slow wake-ups, or usage caps. Check the host's current pricing and terms before deploying. A custom domain is usually separate and may cost money; use the free subdomain supplied by the host.

## Add software
Add another dictionary to `TOOLS` in `app.py`. Set `pricing` to `free` or `paid`, and use the vendor's official URL. Keep pricing labels accurate and recheck them periodically.

## Notes
- This is an independent directory, not an official partner of listed companies.
- Pricing can change. Some products have free tiers and paid upgrades; labels are simplified guides.
- The starter catalog is curated, not literally every editor ever released.
- For public deployment, use the included Gunicorn start command; do not expose Flask's debug server.
