# NRO forwarder

Title: 使命召唤：纳粹僵尸. Publisher: Xiao Fan.
Application ID: 05004E5A505A6000. Target: sdmc:/switch/cod-zombies/cod-zombies.nro.

Uses the bundled NTON hbloader ExeFS from the commit pinned in UPSTREAM.txt. Loader source and its permissive license are retained under rom/. Original ExeFS files are unmodified here; tools/prepare-forwarder.py patches the three NPDM title IDs in dist/ only. No Nintendo executable is used.

Build the game NRO first, then run python3 tools/prepare-forwarder.py. Pack dist/forwarder-ready/{exefs,control,romfs} with hacBrewPack and a private keyset. Do not publish keys.

Place the self-contained NRO at the exact target path and install the forwarder NSP. The forwarder does not include game resources. Subsequent updates replace only that NRO. A forwarder is still an unsigned NSP and requires hardware testing; it does not guarantee resolution of the prior generic startup error.
