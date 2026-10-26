# tv2u-image tools v2.1.14

Complete native Android image-editor source. Opaque ash workspace and slim
metallic icon bars. Android 8.0/API26 minimum; compile/target SDK35.

## Move, draw, then confirm

Import starts in Move mode, with no drawing tool active. Drag with one finger
to move the view; use two fingers to pinch/pan. The hand icon at the top of
the right toolbar returns to Move. Tapping an active drawing tool toggles it off.

Pen (new pencil-and-trace icon), Line, Arrow, Rectangle and Highlighter stay as
previews after finger release. Apply commits the pending strokes; Cancel drops
them. Undo removes the last pending stroke before touching saved history.
Apply/Cancel returns to Move. Switching tools with an unconfirmed drawing
offers Apply / Discard / Keep editing. No image edits are committed by merely
touching a newly imported photo.

## Compact bottom popups

All app-owned menus/settings/confirmations use a shared compact dialog. Popups
are bottom anchored just above the editor's Apply/Cancel row, or above the
bottom action bar when no selection is pending. Their own Cancel / Apply /
Done / Preview / other actions form a centered footer at the bottom of that
popup. The underlying image is only lightly dimmed.

Straighten has one slider row and no repeated label or large padding. Size
combines its number with −/+ in one row. Each RGB label shares its slider row.
Menu rows are compact, and long menus scroll within a capped panel. Width and
height adapt to the available window; the native window resizes for text input.

## Free-form Blur / Unblur

Blur and Unblur are restored in the right toolbar and More → All drawing tools.
Choose either tool, trace an arbitrary outline with ONE finger, and release;
the loop closes automatically. Apply commits only the selected path interior,
not its bounding rectangle. Cancel drops the pending selection; Undo can clear
it or revert a committed mask change. Apply/Cancel returns to Move.

Unblur removes blur added in this editing session and reveals the original
underlying image in that region. It cannot reconstruct an already blurred
imported photo. Two-finger pinch/pan and − / Fit / + are available in these
selection modes too; navigating keeps the lasso coordinates unchanged.

## File Manager Open with

The activity registers ACTION_VIEW for image/* over content/file URIs. Choose
**tv2u-image tools** from a file manager's Open with list. Image loading runs
on a worker and starts in Move. An existing editing session prompts before
opening another image. Android content-URI read access comes from the sender.
The app does not request broad storage permission.

## Editing controls

Size icon: strokes 1–60 source pixels; Text fonts 10–300 pixels. Hold a drawing
tool to open Size as well. Font and stroke sizes are independent.
Text → Add text / Select existing text / Edit selected text. App-added text
remains editable after Apply: drag its box, resize the corner dot, change its
words/color/size, then Apply. Cancel restores it; Undo reverses edits. Text
inside an imported/flattened bitmap is not an editable object.

Crop: More → Select area. Perspective: four independent corners. These and Blur/Unblur support
pinch/pan and a − / Fit / + overlay. Fit shows all corners; ordinary drawing
returns to no-gap cover view. Rotate: 90° left/right. Straighten: ±15° dialog.
Bottom actions: Upload, Share, Search, Print, Copy, Save, Close. PNG preserves
source transparency; JPEG flattens onto white at 95% quality. Upload uses the
Android document/cloud provider; Search uses installed compatible handlers or
a save-then-Lens-web fallback. Copy requires an image-paste-capable app.

The right bar and fixed bottom bar are both 40dp thick, with no outer margin
except system-safe insets. Portrait/landscape supported. Imports downsample
to a 1920px long edge; history and text objects live in memory. Save before exit.

## Complete GitHub package

- `.source.zip` — complete project; upload as a ZIP.
- `.github/workflows/app-debug.yml` — tests, lint and APK build.
- `app-version.txt` — 2.1.14, the source of versionName and APK filename.
- `prepare-source.py`, `source-manifest.json` — paired source checks/extraction.
- `Tutorial/` — Bengali build/use instructions, previews and validation limits.
- `README.md`, `.gitignore`.

Replace ALL files together at the repository root and commit. Use the new run.
Artifact: `tv2u-image-tools-TV2U-EDITOR-R14-APK`.
APK filename: `tv2u-image tools-v2.1.14.apk`. No prebuilt APK is included.

JDK17 / Gradle8.11.1 / AGP8.9.2 / SDK35. Development signing key and optional
private-signing secrets preserved. Test previews use sample content/resources,
not physical-device screenshots. See Tutorial/CODE-VALIDATION.txt.
