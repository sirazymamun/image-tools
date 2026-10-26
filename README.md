# tv2u-image tools v2.1.4 — GitHub package

Source-only package. Read **Tutorial/GITHUB-BUILD-BANGLA.md** first.

| Item | Purpose |
| --- | --- |
| `.source/tv2u-image-tools-source.zip` | Complete Android project source, compressed |
| `.github/workflows/app-debug.yml` | GitHub Actions workflow |
| `app-version.txt` | Single editable app version |
| `Tutorial/` | Bengali build, use, signing and validation instructions |
| `prepare-source.py` | Extracts project and copies root version into it |
| `.gitignore` | Keeps extracted build files out of the repository |

Upload these root items to the root of your GitHub repository. Actions extracts
source automatically into `.build/project`, runs tests/lint, builds the signed
release and uploads `tv2u-image tools-v2.1.4.apk` as an artifact.

The requested workflow filename is `app-debug.yml`; it retains the previous
signed **release** build with the public development key. Optional private
signing secrets are supported. Existing app code and app version are unchanged.
No APK is included. The app background stays opaque white.

Change only the root `app-version.txt` for the next version; the extraction step
copies it into the project before building. GitHub requires workflow YAML files
under `.github/workflows/`, so keep that nested path.
