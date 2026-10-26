# Full-game comparison using hardware-successful A profile

User-provided A log records standard libnx initialization, main entry and console initialization success. B records successful filesystem and application-service initialization, then completion of its intentional ten-second timer and cleanup. B returning HOME in that recorded run is expected behavior.

The standalone game still fails without its boot log. No root cause has been established. A's process metadata differs from the game's in allowed SVCs, service-host declarations, stack size and handle table size.

Controlled comparison: retain A's NPDM and full control directory byte-for-byte (application ID 05004E5A505A8000). Replace ExeFS main with the original 0.1.7 diagnostic full-game NSO and use that game's extracted RomFS. Set CNMT application version to 524288 (0x00080000) in the local hacBrewPack build before packaging. The HOME name intentionally stays NZP 启动检查 A. Installing this candidate replaces probe A; launch that entry to test the full game. B and the original game's application IDs are separate.

The helper tools/prepare-native-a-game.py reproduces the input staging from a retained A staging directory, the game NSO and extracted game RomFS. Packaging still uses the private keyset; no keys are committed.

Verified locally: process/control metadata byte equality with A, game NSO equality with 0.1.7, NCA section integrity, CNMT application ID/version/content sizes/SHA256 references. Hardware startup of this comparison remains untested. Look for sdmc:/nzp-native-boot.log immediately after launching it; report absence too. Do not label this a proven fix.
