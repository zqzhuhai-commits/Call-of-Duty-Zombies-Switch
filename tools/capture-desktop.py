#!/usr/bin/env python3
"""Capture actual desktop verification renders; never label these as Switch footage."""
from pathlib import Path
import os,subprocess,time
root=Path(__file__).resolve().parents[1]
out=root/'screenshots';out.mkdir(exist_ok=True)
engine=root/'engine';binary=engine/'build/sdl/nzportable';data=engine/'romfs'
env=dict(os.environ,SDL_AUDIODRIVER='dummy',LIBGL_ALWAYS_SOFTWARE='1')
base=[str(binary),'-basedir',str(data),'-nosound','-nocdaudio','+vid_width','1280','+vid_height','720','+show_fps','0']
log=(out/'desktop-menu.log').open('w')
p=subprocess.Popen(base,cwd=data,env=env,stdout=log,stderr=subprocess.STDOUT)
try:
 time.sleep(8)
 if p.poll() is not None:raise RuntimeError('Desktop menu process exited; inspect desktop-menu.log')
 subprocess.run(['scrot',str(out/'desktop-01-main-menu.png')],check=True)
 subprocess.run(['xdotool','key','Down','Return'],check=True)
 time.sleep(2)
 subprocess.run(['scrot',str(out/'desktop-02-settings.png')],check=True)
finally:
 p.terminate()
 try:p.wait(timeout=5)
 except subprocess.TimeoutExpired:p.kill();p.wait()
 log.close()
for mapname in ['ndu','nzp_warehouse2']:
 bmp=data/'capture.bmp'
 if bmp.exists():bmp.unlink()
 with (out/f'desktop-{mapname}.log').open('w') as log:
  cmd=base+['+developer','1','+r_retro','1','+host_framerate','0.05','+sys_testmode','1','+map',mapname]
  subprocess.run(cmd,cwd=data,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=90,check=True)
 if not bmp.exists():raise RuntimeError(f'No actual render captured for {mapname}')
 from PIL import Image
 Image.open(bmp).save(out/f'desktop-03-{mapname}.png')
(out/'README.txt').write_text('Actual desktop (Linux/SDL, software OpenGL) verification screenshots of the Chinese adaptation. NOT Nintendo Switch hardware or emulator captures. Gameplay test uses upstream deterministic map-boot mode; it does not verify performance or audio.\n')
