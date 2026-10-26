# 0.1.5 Chinese font correction

Prior Switch build renders 1920x1080, not 1280x720. Its gl_max_size defaults to 256. The shared texture upload code applied this cap to the Chinese atlas too: the 512x256 atlas was downsampled before text drawing. Nearest sampling alone cannot recover discarded strokes.

Changes: render Switch at 1280x720; preserve charset_zh texture dimensions regardless of gl_max_size/gl_picmip; generate a 1024x1024 font atlas with 36-pixel cells and weight 550; retain 12 UI units per Chinese glyph. At 720p the standard UI scale is 3, so each atlas cell maps directly to 36 screen pixels. Text measurement now rounds scale consistently with drawing.

325 translations, including interaction templates translated before button/item expansion, localized costs, survival round totals, scoreboard, round labels, ammo warnings and additional perk/powerup names. Custom map strings and image-based English are not guaranteed complete.

Build/desktop validation is not Switch hardware verification. The 0.1.4 forwarder remains usable: replace sdmc:/switch/cod-zombies/cod-zombies.nro only.
