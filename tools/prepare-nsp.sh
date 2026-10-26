#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
: "${DEVKITPRO:?Set DEVKITPRO}"
export PATH="$DEVKITPRO/tools/bin:$PATH"
test -f dist/NZP-ZH.elf
test -f engine/romfs/nzp/gfx/charset_zh.tga
mkdir -p dist/nsp-ready/exefs
elf2nso dist/NZP-ZH.elf dist/nsp-ready/exefs/main
python3 tools/prepare-application.py
