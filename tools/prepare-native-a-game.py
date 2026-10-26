#!/usr/bin/env python3
"""Prepare a controlled full-game comparison using the successful A profile."""
from pathlib import Path
import argparse,shutil,hashlib,json
p=argparse.ArgumentParser()
p.add_argument('--probe-dir',type=Path,required=True)
p.add_argument('--game-main',type=Path,required=True)
p.add_argument('--game-romfs',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
a=p.parse_args()
if a.output.exists() and any(a.output.iterdir()):raise SystemExit('Use a fresh output directory')
a.output.mkdir(parents=True,exist_ok=True)
shutil.copytree(a.probe_dir/'control',a.output/'control')
(a.output/'exefs').mkdir()
shutil.copyfile(a.probe_dir/'exefs/main.npdm',a.output/'exefs/main.npdm')
shutil.copyfile(a.game_main,a.output/'exefs/main')
shutil.copytree(a.game_romfs,a.output/'romfs')
manifest={str(f.relative_to(a.output)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(a.output.rglob('*')) if f.is_file()}
(a.output/'input-sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Prepared full game with byte-identical A process/control metadata')
