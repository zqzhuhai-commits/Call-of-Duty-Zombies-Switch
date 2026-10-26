#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
: "${DEVKITPRO:?Set DEVKITPRO to the devkitPro installation}"
export DEVKITA64="${DEVKITA64:-$DEVKITPRO/devkitA64}"
export PATH="$DEVKITA64/bin:$DEVKITPRO/tools/bin:$PATH"
test -f engine/romfs/nzp/gfx/charset_zh.tga
test -f engine/romfs/nzp/progs.dat || test -f engine/romfs/nzp/nzp.pak
make -C engine -f Makefile.nx -j2
mkdir -p dist
cp engine/build/nx/bin/nzportable.nro dist/NZP-ZH-Standalone.nro
cp engine/build/nx/bin/nzportable.elf dist/NZP-ZH.elf
cp engine/build/nx/bin/nzportable.nacp dist/NZP-ZH.nacp
sha256sum dist/* > dist/SHA256SUMS.txt
