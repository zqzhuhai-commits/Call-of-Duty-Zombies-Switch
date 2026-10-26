# 0.1.3 verification

Application: 使命召唤：纳粹僵尸. Publisher: Xiao Fan.

The user confirmed the earlier NRO launches on Switch; the earlier NSP does not.
The earlier application ID had bit 0x800 set, which denotes update IDs.
The new NSP uses base application ID 05004E5A505A4000 consistently in NPDM, NACP and NCA/CNMT. This is a candidate launch fix, not hardware-confirmed.

Chinese glyphs now render at their generated 12-pixel size using nearest filtering, instead of shrinking 16 pixels to 10 with linear filtering. 258 translation entries. Dynamic prompts, biographies and texture text remain incomplete.

Passed: Switch CI build, desktop menu/settings capture and two map boot tests, all NCA section integrity checks, CNMT content hashes/sizes, extracted font match, title/publisher/16 icons.

Package SHA256: e13d34a4e92fc2fd572e474c255939989c4bdea88af760e071c5bf77b2024150

Install as a new application; the old failed 05004E5A505A4800 entry can be removed separately. Hardware startup and Chinese legibility require user testing.
