# Icon loading investigation / 0.1.2

User reported an endlessly loading HOME tile and inability to launch.

Verified old package properties:
- Both packaged icons were 256x256 progressive JPEG images.
- NACP language mask was 0x0BFF; Simplified Chinese bit 14 was unset.
- Only AmericanEnglish and SimplifiedChinese icon files existed, while other languages were advertised.

Changes:
- New 256x256 baseline JPEG, no EXIF metadata.
- 16 matching language entries, language bits and icon files.
- Display name 使命召唤：僵尸; publisher Xiao Fan.
- Display version 0.1.2, CNMT application version 131072 (requires corresponding hacBrewPack cnmt_create modification).
- Title ID unchanged: 05004E5A505A4800.

Verified: all NCA section integrity checks, CNMT Program/Control content IDs, content sizes and SHA256 values, extracted control metadata and icon decoding.

Not verified: HOME tile rendering or game startup on Switch hardware. The observed old-package properties are suspected contributors; the root cause is not yet confirmed.

NSP SHA256: b47f9cc36d2e1e7b4496e38492e5cf8aec877121921b77446ef4ff9b0e0809df
