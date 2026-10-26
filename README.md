# tv2u-image tools v2.1.6 — LIGHTSHOT L6

Complete source-only package. No prebuilt APK. Minimum Android **8.0 (API 26)**,
with no maximum SDK restriction. White opaque background, compact Lightshot-style
selection border/handles, floating drawing rail and floating action bar.

## Exact visible tool set

Lightshot drawing items: **Pen, Line, Arrow, Rectangle, Highlighter, Text, Color,
Undo**. Lightshot bottom items: **Upload, Share, Search, Print, Copy, Save, Close**.
Only three extra editing tools: **Rotate, Straighten, Perspective Crop**.
Import and Select area are the Android image/selection entry points.

Pen/stroke width: **1–60 image pixels**. Use the portrait slider or hold the Pen
icon; the width dialog also works in landscape. Text size uses the same control.
Rotate turns 90° left/right. Straighten has a separate −15° to +15° slider.
Perspective Crop lets four corners move independently, then rectifies the convex
quadrilateral into a straight rectangle. Apply commits it; Undo restores it.

Responsive layout: vertical floating rail in portrait, compact grid in landscape.
The action bar follows the selection and stays within the available screen.
Landscape puts width settings in the Pen hold dialog / header More menu.
Orientation changes preserve the current image and selection coordinates.

Upload writes PNG to the chosen Android document provider; choose an installed
cloud provider to upload. It does not create a public Lightshot/prnt.sc link.
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
| `app-version.txt` | Version source, currently 2.1.6 |
| `prepare-source.py` | Source identity/checksum verification and extraction |
| `source-manifest.json` | Checksum paired with this exact source ZIP |
| `README.md`, `.gitignore` | Guide and generated-output exclusions |
| `Tutorial/` | Bengali instructions, previews, validation |

Upload **ALL root items together**. Changing app-version.txt alone does not
replace the UI. The helper rejects old/mixed source archives. Header identity:
**LIGHTSHOT L6**. Actions artifact: **tv2u-image-tools-LIGHTSHOT-L6-APK**.
Output filename: **tv2u-image tools-v2.1.6.apk**.

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
background itself stays white and opaque.
