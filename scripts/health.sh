#!/usr/bin/env bash
# Health runner — Mourad.Soltani
set -euo pipefail
cd "$(dirname "$0")/.."
python -m pytest tests/test_health.py -q
echo "SoltaniHunt health OK — Mourad.Soltani"
