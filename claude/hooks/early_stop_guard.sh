#!/usr/bin/env bash
set -euo pipefail
input="${1:-}"
if printf '%s' "$input" | grep -Eiq "(I would|I'll|should work|not tested|test later|나중에 테스트)"; then
  echo "early-stop language detected"
  exit 1
fi
