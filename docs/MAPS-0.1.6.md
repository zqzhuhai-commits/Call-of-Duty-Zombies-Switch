# Map metadata localization / 0.1.6

All 19 bundled maps now have Chinese display names and descriptions. BSP identifiers, filenames, author credits, thumbnail flags and game-setting flags are preserved. Localized metadata is copied after extracting pinned upstream resources; map overrides remain subject to their original CC BY-SA asset license.

Up to six description lines per map, each under the engine 64-byte field limit; description spacing is 12 UI units. Font glyph generation includes localized map metadata. Selection, lobby, load-screen and scoreboard names share these metadata fields. Newly added third-party maps without localizations remain in their original language.

The 720p renderer and unscaled Chinese atlas from 0.1.5 remain. Existing forwarder target path is unchanged.
