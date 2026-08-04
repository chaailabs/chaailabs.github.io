# Chaai Labs website and documentation

This repository builds the Chaai Labs landing page and public Chaai–HPCA documentation.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-docs.txt
bash scripts/validate_public_docs.sh
bash scripts/build_site.sh
python -m http.server 8000 --directory _site
```

Only reviewed public content belongs here. Credentials, internal paths, infrastructure details, live workloads, unpublished results, and partner information are prohibited.

