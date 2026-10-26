# Native NSP startup candidate / 0.1.6

Program and RomFS are embedded in the NSP; no external NRO is referenced. Includes all 19 localized map descriptions and the 720p/full-resolution font changes.

Relative to the failed 0.1.3 package, the process CPU range is now 0..2 rather than 0..3, and the address-space setting is 36-bit rather than 39-bit, matching the bundled hbloader application's settings. These are candidate compatibility changes, not a confirmed diagnosis.

Application ID stays 05004E5A505A4000. Display version is 0.1.6; apply packaging/hacbrewpack-v016.patch to the upstream packer to set CNMT version 393216. Keys remain private and are not part of this repository.

Structural validation is not proof of installation or startup on hardware. The previous generic startup error remains unresolved until this build is tested by the user.
