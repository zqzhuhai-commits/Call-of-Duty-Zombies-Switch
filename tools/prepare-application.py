#!/usr/bin/env python3
"""Prepare 0.2.0 metadata using the hardware-verified native A profile."""
from pathlib import Path
import base64,shutil,struct
root=Path(__file__).resolve().parents[1]
out=root/'dist/nsp-ready'
(out/'exefs').mkdir(parents=True,exist_ok=True)
(out/'control').mkdir(parents=True,exist_ok=True)
npdm=base64.b64decode((root/'packaging/working-application.npdm.b64').read_bytes())
assert npdm.count(struct.pack('<Q',0x05004E5A505A8000))==3
(out/'exefs/main.npdm').write_bytes(npdm)
control=bytearray(base64.b64decode((root/'packaging/working-application-control.nacp.b64').read_bytes()))
assert len(control)==0x4000
for i in range(16):
 off=i*0x300
 control[off:off+0x200]='使命召唤：纳粹僵尸'.encode().ljust(0x200,b'\0')
 control[off+0x200:off+0x300]=b'Xiao Fan'.ljust(0x100,b'\0')
control[0x3060:0x3070]=b'0.2.0'.ljust(16,b'\0')
assert struct.unpack_from('<Q',control,0x3038)[0]==0x05004E5A505A8000
(out/'control/control.nacp').write_bytes(control)
langs=['AmericanEnglish','BritishEnglish','Japanese','French','German','LatinAmericanSpanish','Spanish','Italian','Dutch','CanadianFrench','Portuguese','Russian','Korean','TraditionalChinese','SimplifiedChinese','BrazilianPortuguese']
for lang in langs:shutil.copyfile(root/'art/cod-zombies-icon-256.jpg',out/f'control/icon_{lang}.dat')
print('Prepared release title and byte-identical hardware-verified native process profile')
