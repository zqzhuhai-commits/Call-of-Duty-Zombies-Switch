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
nacptool --create '使命召唤：纳粹僵尸' 'Xiao Fan' '0.1.6' dist/nsp-ready/control/control.nacp --titleid=05004E5A505A4000
cp art/cod-zombies-icon-256.jpg dist/nsp-ready/control/icon_AmericanEnglish.dat
cp art/cod-zombies-icon-256.jpg dist/nsp-ready/control/icon_SimplifiedChinese.dat
printf '%s\n' 'NSO/NPDM/NACP prepared. NSP encryption/packaging and hardware testing are still pending.'

# Match declared languages to actual baseline-JPEG control icons.
python3 - <<'PYLANG'
from pathlib import Path
import struct, shutil
control=Path('dist/nsp-ready/control')
p=control/'control.nacp';d=bytearray(p.read_bytes());struct.pack_into('<I',d,0x302c,0xffff);p.write_bytes(d)
langs=['AmericanEnglish','BritishEnglish','Japanese','French','German','LatinAmericanSpanish','Spanish','Italian','Dutch','CanadianFrench','Portuguese','Russian','Korean','TraditionalChinese','SimplifiedChinese','BrazilianPortuguese']
for lang in langs:shutil.copyfile('art/cod-zombies-icon-256.jpg',control/f'icon_{lang}.dat')
PYLANG
