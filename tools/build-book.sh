#!/usr/bin/env bash
#
# build-book.sh — build the textbook locally with mdBook.
#
# Output goes to ./book/ (gitignored). For live-reload during
# editing, run `mdbook serve` from the repo root instead.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

if ! command -v mdbook >/dev/null 2>&1; then
    cat >&2 <<'MSG'
Error: mdbook is not installed.

Install it with one of:
  cargo install mdbook
  brew install mdbook
  (or see https://rust-lang.github.io/mdBook/guide/installation.html)
MSG
    exit 1
fi

mdbook build

echo
echo "Built textbook to ${REPO_ROOT}/book/"
echo "Open ${REPO_ROOT}/book/index.html in a browser, or run:"
echo "  mdbook serve"
echo "from the repo root for live-reload during editing."
