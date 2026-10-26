# 使命召唤：纳粹僵尸 0.2.0

Publisher: Xiao Fan. Native application ID: 05004E5A505A8000. CNMT version: 589824 (0x00090000). This updates the successful A full-game comparison in place and restores the proper HOME title. It embeds its native program and all game assets, without an external NRO.

The user confirmed both main-menu entry and starting gameplay using the A-profile full-game comparison. Keep that process profile byte-for-byte; retain its control data except displayed titles/publisher/version. The checked-in base64 files contain generated application metadata only, not keys. packaging/npdm.json is an earlier investigation profile and is not used by the release preparation tool.

Retain 1280x720 rendering, full-resolution Chinese atlas and Chinese names/descriptions for all 19 bundled maps. Incomplete translation still includes character biographies, some textures and map-specific prompts.

Switch gyro defaults to enabled. After the ordinary startup configuration runs, a one-time migration enables an older disabled gyro setting and immediately saves an archived version marker. Existing ADS-only mode and sensitivity choices remain; later manually disabling gyro is respected. Settings path: 设置 -> 操作 -> 体感瞄准.

The new default-gyro migration and 0.2.0 metadata require fresh hardware feedback; the prior complete-game startup path is the hardware-verified baseline. Do not claim all maps, audio, long-session stability or new gyro settings were exhaustively hardware-tested.

NSP packaging: build source, run tools/prepare-nsp.sh, apply packaging/hacbrewpack-v020.patch to the upstream packer, then package nsp-ready exefs/control plus the matching embedded game RomFS using a private keyset. Keys are never stored in the repository. NRO forwarder target remains sdmc:/switch/cod-zombies/cod-zombies.nro.
