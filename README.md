v2.1.8 / PHOTO EDITOR: ash-gray theme, equal 40dp bars, fixed bottom actions and flush-right vertical tools.

# tv2u-image tools v2.1.8 — PHOTO EDITOR

Complete source-only package. No prebuilt APK. Minimum Android **8.0 (API 26)**,
with no maximum SDK restriction. Opaque ash-gray background, compact compact
selection border/handles, flush-right drawing rail and fixed bottom action bar.

## Available tools

Drawing tools: **Pen, Line, Arrow, Rectangle, Highlighter, Text, Color,
Undo**. Bottom actions: **Upload, Share, Search, Print, Copy, Save, Close**.
Only three extra editing tools: **Rotate, Straighten, Perspective Crop**.
Import and Select area are the Android image/selection entry points.

Pen/stroke width: **1–60 image pixels**. Use the portrait slider or hold the Pen
icon; the width dialog also works in landscape. Text size uses the same control.
Rotate turns 90° left/right. Straighten has a separate −15° to +15° slider.
Perspective Crop lets four corners move independently, then rectifies the convex
quadrilateral into a straight rectangle. Apply commits it; Undo restores it.

Responsive layout: a 40dp-wide single-column rail touches the right safe edge in
both orientations. Scroll to reach tools on short screens. The 40dp-high action
bar stays at the bottom below all editing controls; selection never moves it.
Icons are enlarged (up to 34dp) with no visible duplicate text labels. Tooltip
and accessibility names remain available. Only system cutout/navigation safe
insets are respected; no added screen-edge margin surrounds the rail.
Landscape puts width settings in the Pen hold dialog / header More menu.
Orientation changes preserve the current image and selection coordinates.

Upload writes PNG to the chosen Android document provider; choose an installed
cloud provider to upload. It does not create a public public image-hosting link.
Search sends the image to an installed compatible Lens/search handler. Without
one, it asks you to save PNG, then opens Lens web so you can select the saved
image. External services need their own apps/accounts/network as appropriate.
Print opens Android printing, including Save as PDF. Copy needs a receiving app
that accepts image paste. Images are not sent outside before the user acts.

## Complete repository layout

| Root item | Purpose |
| --- | --- |
| `.source.zip` | Complete Android source, keep zipped |
| `.github/workflows/app-debug.yml` | Test/lint/build workflow |
| `app-version.txt` | Version source, currently 2.1.8 |
| `prepare-source.py` | Source identity/checksum verification and extraction |
| `source-manifest.json` | Checksum paired with this exact source ZIP |
| `README.md`, `.gitignore` | Guide and generated-output exclusions |
| `Tutorial/` | Bengali instructions, previews, validation |

Upload **ALL root items together**. Changing app-version.txt alone does not
replace the UI. The helper rejects old/mixed source archives. Header identity:
**PHOTO EDITOR**. Actions artifact: **tv2u-image-tools-TV2U-EDITOR-R8-APK**.
Output filename: **tv2u-image tools-v2.1.8.apk**.

The same signing key/secrets remain supported. SDK setup explicitly requests
platform-tools, retaining the obsolete-tools fix. Build: JDK 17, SDK 35, Build
Tools 35.0.0, Gradle 8.11.1, AGP 8.9.2. Target SDK 35 does not impose a maximum
Android version. Runtime calls introduced later than Android 8 are guarded;
Android 8/8.1 uses BitmapFactory + EXIF orientation instead of ImageDecoder.

Preview PNGs are rendered Android UI using a sample image and test resources,
not screenshots from a physical phone. See validation notes for tested scope.
Image processing/encoding runs on a worker; history stores small commands.
Imports use a maximum 1920-pixel long edge. Sessions are in memory; save before
leaving. PNG preserves source transparency, JPEG exports onto white; the app
background itself stays ash-gray and opaque.
