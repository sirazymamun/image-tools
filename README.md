# tv2u-image tools v2.1.5 — Lightshot-inspired Android editor

Source-only GitHub package. No prebuilt APK. Android 10+.

## Same repository layout

| Root item | Purpose |
| --- | --- |
| `.source.zip` | Complete Android source; upload without extracting |
| `.github/workflows/app-debug.yml` | Test, lint and APK build pipeline |
| `app-version.txt` | Version source, currently 2.1.5 |
| `prepare-source.py` | Extracts root source ZIP and copies version |
| `README.md` | This overview |
| `.gitignore` | Excludes extracted build output |
| `Tutorial/` | Bengali build, tools and validation guides |

## Lightshot-inspired interface

Opaque white background, a compact icon rail beside the image and a bottom
action bar. Long-press an icon for its tool name; scroll the rail on short
screens. Color stays pinned below the tool rail. Crop shows resize handles,
selection dimensions and a dimmed image outside the selection.

Drawing tools: Pen, Line, **Arrow**, Rectangle, translucent Highlighter, Text,
Blur, Unblur, Crop and Rotate/Straighten. Drag to preview a shape; release to
commit. Color and width apply to annotations. Crop/text use Apply/Cancel.
Bottom actions: Undo, Redo, Copy image, Save, Share. Import stays in the header.
Copy uses Android's image clipboard; pasting depends on the receiving app.
No Windows-only cloud search, printing or public screenshot upload is added.

The previous background renderer, command undo/redo, PNG/JPEG export and
private image-sharing provider remain in use. No image encoding is done in
`onDraw` or lifecycle callbacks. Imports have a maximum 1920-pixel long edge.
Blur/unblur affects the source image layer and preserves annotations. Unblur
cannot recover information blurred before import. Working state is in memory;
save before leaving. PNG preserves source transparency; the app background
itself is opaque white. Rotated images can be cropped to remove empty corners.

## GitHub build

Upload this ZIP's extracted ROOT CONTENTS into the repository root, including
`.source.zip` and `.github/workflows/app-debug.yml`. Keep `.source.zip` zipped.
Actions → Build tv2u-image tools APK → Run workflow.
Artifact APK: `tv2u-image tools-v2.1.5.apk`.
The setup-android step explicitly requests `platform-tools`, preserving the
fix for the removed `tools` package. Existing signing key/secrets are retained.

JDK 17, SDK 35, Build Tools 35.0.0, Gradle 8.11.1, AGP 8.9.2.
Only JUnit/Robolectric test dependencies are external app libraries; the running
app uses Android APIs and works offline. See Tutorial for all build details.
