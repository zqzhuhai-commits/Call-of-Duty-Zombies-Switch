#!/usr/bin/env python3
"""Prepare the bundled NTON hbloader forwarder without using private keys."""
from pathlib import Path
import hashlib,json,shutil,struct
ROOT=Path(__file__).resolve().parents[1]
base=ROOT/'forwarder/nton/assets/exefs'
out=ROOT/'dist/forwarder-ready'
for sub in ['exefs','control','romfs']:(out/sub).mkdir(parents=True,exist_ok=True)
shutil.copyfile(base/'main',out/'exefs/main')
npdm=bytearray((base/'main.npdm').read_bytes())
old=struct.pack('<Q',0x010e3d7237302000);newid=0x05004E5A505A6000
assert npdm.count(old)==3, 'Unexpected upstream NPDM; review before changing IDs'
(out/'exefs/main.npdm').write_bytes(npdm.replace(old,struct.pack('<Q',newid)))
nacp=bytearray((ROOT/'dist/NZP-ZH.nacp').read_bytes());assert len(nacp)==0x4000
for i in range(16):
 off=i*0x300
 nacp[off:off+0x200]='使命召唤：纳粹僵尸'.encode().ljust(0x200,b'\0')
 nacp[off+0x200:off+0x300]=b'Xiao Fan'.ljust(0x100,b'\0')
struct.pack_into('<I',nacp,0x302c,0xffff)
nacp[0x3025]=0 # no user selection
nacp[0x3060:0x3070]=b'0.1.4'.ljust(16,b'\0')
for off in [0x3038,0x3078,0x30b0]:struct.pack_into('<Q',nacp,off,newid)
struct.pack_into('<Q',nacp,0x3070,newid+0x1000)
for off in [0x3080,0x3088,0x3090,0x3098,0x30a0,0x3148,0x3150,0x3158,0x3160,0x3168,0x3170,0x3178,0x3180]:struct.pack_into('<Q',nacp,off,0)
struct.pack_into('<H',nacp,0x3188,0)
(out/'control/control.nacp').write_bytes(nacp)
langs=['AmericanEnglish','BritishEnglish','Japanese','French','German','LatinAmericanSpanish','Spanish','Italian','Dutch','CanadianFrench','Portuguese','Russian','Korean','TraditionalChinese','SimplifiedChinese','BrazilianPortuguese']
for lang in langs:shutil.copyfile(ROOT/'art/cod-zombies-icon-256.jpg',out/f'control/icon_{lang}.dat')
path='sdmc:/switch/cod-zombies/cod-zombies.nro'
for name in ['nextNroPath','nextArgv']:(out/'romfs'/name).write_text(path)
manifest={'application_id':f'{newid:016X}','target':path,'loader':(ROOT/'forwarder/UPSTREAM.txt').read_text().splitlines(),'sha256':{str(p.relative_to(out)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.rglob('*')) if p.is_file()}}
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Prepared NRO forwarder:',path)
