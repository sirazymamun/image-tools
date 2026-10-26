# tv2u-image tools v2.1.4 — GitHub root source package

This package matches the requested repository layout. **No prebuilt APK.**

| Root item | Purpose |
| --- | --- |
| `.source.zip` | Complete Android source project; keep it zipped |
| `.github/workflows/app-debug.yml` | GitHub Actions workflow |
| `app-version.txt` | Editable app version, currently 2.1.4 |
| `prepare-source.py` | Opens the ROOT `.source.zip` and copies root version |
| `README.md` | This guide |
| `.gitignore` | Excludes extracted build files |
| `Tutorial/` | Bengali build/use/signing instructions |

Upload ALL these items to the repository root. Do not upload the outer package
ZIP as a single file. Do not extract `.source.zip` before uploading.

Actions → Build tv2u-image tools APK → Run workflow.
The workflow extracts source into `.build/project`, runs tests/lint, builds the
signed release, and uploads an artifact containing `tv2u-image tools-v2.1.4.apk`.
The workflow filename is `app-debug.yml`, retaining the same release build.
Root `.source.zip` replaces the older `.source/` directory arrangement. The
script already uses the correct path; no manual code/path editing is needed.

Only root `app-version.txt` needs editing for a new version. The app source and
signing key are unchanged from v2.1.4. Optional private signing secrets remain
supported. See Tutorial/GITHUB-BUILD-BANGLA.md for beginner instructions.
