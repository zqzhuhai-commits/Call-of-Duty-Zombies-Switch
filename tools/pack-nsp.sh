#!/usr/bin/env bash
# Run locally with a private keyset. Never commit keys or print their contents.
set -euo pipefail
cd "$(dirname "$0")/.."
if [ "$#" -ne 1 ]; then
  echo 'Usage: bash tools/pack-nsp.sh /absolute/path/to/prod.keys' >&2
  exit 2
fi
keyset=$(realpath "$1")
test -f "$keyset"
command -v hacbrewpack >/dev/null
bash tools/prepare-nsp.sh
# Fresh staging avoids reusing stale NCAs. No destructive cleanup of user paths.
staging=$(mktemp -d)
hacbrewpack -k "$keyset" --nologo \
  --exefsdir "$PWD/dist/nsp-ready/exefs" \
  --romfsdir "$PWD/engine/romfs" \
  --controldir "$PWD/dist/nsp-ready/control" \
  --tempdir "$staging/temp" --ncadir "$staging/nca" --nspdir "$PWD/dist/nsp"
find dist/nsp -type f -name '*.nsp' -exec sha256sum {} \;
