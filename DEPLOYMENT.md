# Deployment

## Preconditions

1. Revoke the previously exposed GitHub token.
2. Confirm institutional public-release authorization.
3. Review `PUBLICATION_RISK_REPORT.md` and approve the public content.
4. Ensure the repository remote uses SSH and contains no embedded credential.

## Review locally

```bash
bash scripts/validate_public_docs.sh
python -m pip install -r requirements-docs.txt
bash scripts/build_site.sh
python -m http.server 8000 --directory _site
```

Review `/` and `/docs/` in the local server.

## Publish

### Guarded one-command publisher

Run from an authenticated login shell:

```bash
bash /projects/nmclps/chaailabs-site-integration/publish_phase1.sh
```

The script refuses to continue if the destination is dirty, the remote is not the expected token-free SSH URL, the current branch is not `master`, or the publication branch already exists. It fast-forwards from the remote, creates a review branch, validates public content, commits, and pushes. It never merges or pushes directly to `master`.

### Manual alternative

Copy the reviewed repository contents into the website repository on a branch. Do not copy `.git`, `_site`, `build`, or `.venv`.

```bash
git switch -c integrate-hpca-docs
git add .
git commit -m "Integrate Chaai and HPCA public documentation"
git push --set-upstream origin integrate-hpca-docs
```

Open a pull request into `master`. Require the validation workflow to pass, review the preview artifact, then merge. In repository Settings → Pages, select **GitHub Actions** as the source. The deployment workflow publishes the landing page at `/` and documentation at `/docs/`.
