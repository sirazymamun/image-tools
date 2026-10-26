# tv2u-image tools v2.1.10

Opaque ash-gray Android image editor with beveled metallic toolbars. Minimum Android 8.0 (API 26); target/compile SDK35.

The image fills the working area without top/bottom letterboxing or stretching.
The view shows a zoomed portion of the source. Use TWO fingers to pan/pinch
(1x cover scale to 8x); ONE finger draws or moves selection handles. Navigation
does not crop the document. Save/share/print/copy still use the complete edited
bitmap; only applying Crop/Perspective changes the document dimensions.

The bars have a subtle silver-gray bevel, one outer border, transparent icon
buttons, a compact color swatch and separators at Undo/Close.
The right rail is flush with the safe screen edge and 40dp wide. The bottom
action bar is fixed at the bottom and 40dp high. Icons have no duplicate labels.
System cutout/navigation insets remain respected. Orientation changes preserve
the image, history and current selection.

Pen, Line, Arrow, Rectangle, Highlighter, Text, Color, Undo, Rotate, Straighten,
Perspective Crop. Bottom actions: Upload, Share, Search, Print, Copy, Save, Close.
Import loads an image; More → Select area starts a regular crop.

Use the visible Size (three-sliders) icon above Color to adjust 1–60px strokes,
or 10–300px fonts in Text mode. Tap the selected Pen/Line/Arrow tool again, or
hold any drawing tool, to open size settings. Stroke and font sizes are independent.
App-added text remains selectable after Apply: Text → Select / move existing text,
then tap it or choose it in the list. Drag its box to move; drag the corner dot
to resize. Text → Edit selected text changes its words; Apply commits, Cancel
restores. Undo/redo keep text edits, including after crop/rotate/perspective.
Existing lettering inside an imported bitmap is not an editable text layer.
Reimporting a saved PNG/JPEG starts a new flattened image, without text objects.
Straighten opens its
slider in a dialog with Apply/Cancel. Width/status/angle rows no longer occupy
permanent space below the canvas. Text and crop previews show Apply/Cancel only
while needed. Image processing runs in a worker. Imports are limited to a
1920px long edge. Save before leaving; unsaved sessions are in memory.

PNG preserves image transparency; JPEG flattens onto white at 95% quality.
Upload opens Android's document provider; choose an installed cloud provider.
Search uses compatible installed handlers or a save-then-Lens-web fallback.
Copy requires an app supporting image paste. Print uses Android print services.

## Complete GitHub package

- `.source.zip`: complete Android project; keep zipped when uploading.
- `.github/workflows/app-debug.yml`: test/lint/build workflow.
- `app-version.txt`: 2.1.10; copied into the extracted Android project.
- `prepare-source.py`, `source-manifest.json`: extract and validate paired source.
- `Tutorial/`: Bengali build/use instructions, previews and validation limits.
- `README.md`, `.gitignore`.

Upload ALL files together at the repository root, then commit. Download the
new successful run's `tv2u-image-tools-TV2U-EDITOR-R10-APK` artifact.
APK name: `tv2u-image tools-v2.1.10.apk`. No prebuilt APK is included.

Build toolchain: JDK17, Gradle8.11.1, AGP8.9.2, SDK35/Build Tools35.0.0.
The existing development signing key and optional private-signing secrets are
preserved. Previews use sample images/test resources, not physical-device
screenshots. See Tutorial/CODE-VALIDATION.txt for tested scope.
