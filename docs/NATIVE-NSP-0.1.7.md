# Native startup diagnostics / 0.1.7

User confirmed that the NSP forwarder opens the NRO, while standalone 0.1.6 still fails. Earlier CPU/address-space changes did not resolve the hardware failure. No root cause is claimed.

ELF SVC-wrapper comparison found ReturnFromException linked but not permitted; add SVC 0x28. This is not established as the startup cause.

The weak libnx userAppInit hook now opens a diagnostic log after libnx initialization and SD mounting. Separate logs: sdmc:/nzp-native-boot.log and sdmc:/nzp-nro-boot.log. Each checkpoint closes the file so preceding stages survive a later crash. Checkpoints cover main, input, RomFS result, game heap, Host_Init, EGL initialization/context, GL symbol loading and first frame. Failure before this hook or inability to write SD can leave no log.

All 19 Chinese map metadata files, 720p and the full-resolution Chinese atlas remain unchanged. The NSP embeds the native NSO and game resources; no external NRO is needed. Apply hacbrewpack-v017.patch for CNMT version 458752.

Still requires hardware testing. Delete any older native log before one standalone launch attempt and report the resulting file or its absence. A successful forwarder launch by itself does not validate standalone initialization.
