#!/usr/bin/env python3
"""Verify bundled source identity and checksum before extracting the Android project."""
from pathlib import Path
import hashlib
import json
import re
import sys
import zipfile

ROOT=Path(__file__).resolve().parent
ARCHIVE=ROOT/'.source.zip'
MANIFEST=ROOT/'source-manifest.json'
LAYOUT='TV2U-EDITOR-R13'
version=(ROOT/'app-version.txt').read_text(encoding='utf-8').strip()
if not re.fullmatch(r'\d+\.\d+\.\d+',version):
    raise SystemExit('app-version.txt must contain major.minor.patch, e.g. 2.1.13')
parts=[int(v) for v in version.split('.')]
if parts[0]>1999 or parts[1]>999 or parts[2]>999:
    raise SystemExit('Version limits: major <=1999, minor/patch <=999')
if not ARCHIVE.is_file():
    raise SystemExit('Missing .source.zip. Upload ALL root files from the complete package.')
digest=hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
with zipfile.ZipFile(ARCHIVE) as archive:
    main_name='app/src/main/java/com/tv2u/imagetools/MainActivity.java'
    required=['app/src/main/java/com/tv2u/imagetools/TextLayer.java','app/src/main/java/com/tv2u/imagetools/ToolbarSkin.java','settings.gradle','editor-layout.txt',main_name,'scripts/verify_layout.py','app/src/main/java/com/tv2u/imagetools/ImageSearch.java','app/src/main/java/com/tv2u/imagetools/ImagePrinter.java','app/src/main/java/com/tv2u/imagetools/PerspectiveWarp.java','app/src/main/java/com/tv2u/imagetools/ImageLoader.java']
    for name in required:
        if name not in archive.namelist():
            raise SystemExit('Wrong source ZIP: missing '+name+'. Upload the latest complete package.')
    if archive.read('editor-layout.txt').decode().strip()!=LAYOUT or 'LAYOUT_ID="TV2U-EDITOR-R13"' not in archive.read(main_name).decode():
        raise SystemExit('Old editor source found. A version number change does not update the UI. Upload ALL files from the latest package.')
    if '--refresh-manifest' in sys.argv:
        MANIFEST.write_text(json.dumps({'layout':LAYOUT,'source_zip':'.source.zip','sha256':digest},indent=2)+'\n')
    if not MANIFEST.is_file():
        raise SystemExit('Missing source-manifest.json. Upload it from the SAME full package as .source.zip.')
    expected=json.loads(MANIFEST.read_text())
    if expected.get('layout')!=LAYOUT or expected.get('sha256')!=digest:
        raise SystemExit('Source checksum mismatch. Replace .source.zip AND source-manifest.json from the SAME latest package.')
    target=ROOT/'.build'/'project'
    target.mkdir(parents=True,exist_ok=True)
    for item in archive.infolist():
        if not (target/item.filename).resolve().is_relative_to(target.resolve()):
            raise SystemExit('Invalid path in source ZIP')
    if archive.testzip() is not None:
        raise SystemExit('Source ZIP integrity check failed')
    archive.extractall(target)
(target/'app-version.txt').write_text(version+'\n',encoding='utf-8')
wrapper=target/'gradlew'
if wrapper.exists():wrapper.chmod(wrapper.stat().st_mode|0o111)
print('Verified '+LAYOUT+'; source SHA-256 '+digest)
print('Source prepared at .build/project; version '+version)
