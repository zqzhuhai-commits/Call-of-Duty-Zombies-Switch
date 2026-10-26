#!/usr/bin/env python3
"""Prepare the pinned engine, apply modifications, and embed verified game data."""
from pathlib import Path
import base64,gzip,hashlib,shutil,subprocess,urllib.request,zipfile,argparse,json
ROOT=Path(__file__).resolve().parents[1]
ENGINE_SHA='ac0a0ac6b081be3b44e669dafe842b21b2a033d1'
ASSET_SHA256='7fdae8c41f1e3cd97539e7f0d30e4e201294c077d39e48afc33bb2c003be68ce'
p=argparse.ArgumentParser();p.add_argument('--assets-zip',type=Path);p.add_argument('--skip-assets',action='store_true');a=p.parse_args()
engine=ROOT/'engine'
if not engine.exists():
 subprocess.run(['git','clone','https://github.com/nzp-team/vril-engine.git',str(engine)],check=True)
if subprocess.check_output(['git','status','--porcelain'],cwd=engine).strip():
 raise SystemExit('engine/ has changes. Reuse it for building, or move it aside before preparing again.')
subprocess.run(['git','checkout','--detach',ENGINE_SHA],cwd=engine,check=True)
subprocess.run(['git','apply',str(ROOT/'patches/0001-zh-romfs.patch')],cwd=engine,check=True)
shutil.copytree(ROOT/'overlay/source',engine/'source',dirs_exist_ok=True)
romfs=engine/'romfs';(romfs/'nzp/gfx').mkdir(parents=True,exist_ok=True)
if not a.skip_assets:
 archive=a.assets_zip or ROOT/'downloads/nzportable-switch.zip'
 archive.parent.mkdir(parents=True,exist_ok=True)
 if not archive.exists():
  urllib.request.urlretrieve('https://github.com/nzp-team/nzportable/releases/download/nightly/nzportable-switch.zip',archive)
 if hashlib.sha256(archive.read_bytes()).hexdigest()!=ASSET_SHA256:
  raise SystemExit('Asset ZIP hash differs from the audited 2026-10-22 nightly. Refusing to silently change versions.')
 with zipfile.ZipFile(archive) as z:
  for item in z.infolist():
   prefix='nzportable/nzp/'
   if item.is_dir() or not item.filename.startswith(prefix):continue
   rel=Path(item.filename[len(prefix):])
   if rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe ZIP member')
   dest=romfs/'nzp'/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(item))
 atlas=ROOT/'overlay/romfs/nzp/gfx/charset_zh.tga.gz.b64'
 (romfs/'nzp/gfx/charset_zh.tga').write_bytes(gzip.decompress(base64.b64decode(atlas.read_bytes())))
 (romfs/'nzp/licenses').mkdir(parents=True,exist_ok=True)
 shutil.copy(ROOT/'localization/OFL-NotoSansSC.txt',romfs/'nzp/licenses/OFL-NotoSansSC.txt')
 shutil.copy(ROOT/'LICENSE',romfs/'nzp/licenses/zh-engine-GPL.txt')
 print('Engine and embedded assets prepared. No executable has been built yet.')
else:print('Engine prepared without resources (for source checks only).')
