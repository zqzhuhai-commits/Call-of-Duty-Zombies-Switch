#!/usr/bin/env bash
# Prepare installable-application metadata. Does not create an NSP or read keys.
set -euo pipefail
cd "$(dirname "$0")/.."
: "${DEVKITPRO:?Set DEVKITPRO}"
export PATH="$DEVKITPRO/tools/bin:$PATH"
test -f dist/NZP-ZH.elf
test -f engine/romfs/nzp/gfx/charset_zh.tga
mkdir -p dist/nsp-ready/exefs dist/nsp-ready/control
elf2nso dist/NZP-ZH.elf dist/nsp-ready/exefs/main
npdmtool packaging/npdm.json dist/nsp-ready/exefs/main.npdm
nacptool --create 'NZP 僵尸生存 中文版' 'NZP Team / Xiao Fan' '0.1.0' dist/nsp-ready/control/control.nacp --titleid=05004E5A505A4800
cp engine/source/platform/nx/art/icon.jpg dist/nsp-ready/control/icon_AmericanEnglish.dat
cp engine/source/platform/nx/art/icon.jpg dist/nsp-ready/control/icon_SimplifiedChinese.dat
printf '%s\n' 'NSO/NPDM/NACP prepared. NSP encryption/packaging and hardware testing are still pending.'
