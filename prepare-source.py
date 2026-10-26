#!/usr/bin/env python3
"""Extract the bundled project and copy the authoritative root version file."""
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parent
version = (ROOT / 'app-version.txt').read_text(encoding='utf-8').strip()
if not re.fullmatch(r'\d+\.\d+\.\d+', version):
    raise SystemExit('app-version.txt must contain major.minor.patch, e.g. 2.1.4')
parts = [int(p) for p in version.split('.')]
if parts[0] > 1999 or parts[1] > 999 or parts[2] > 999:
    raise SystemExit('Version limits: major <=1999, minor/patch <=999')
target = ROOT / '.build' / 'project'
target.mkdir(parents=True, exist_ok=True)
archive_path = ROOT / '.source.zip'
if not archive_path.is_file():
    raise SystemExit('Missing .source.zip: upload .source.zip to the repository root beside prepare-source.py')
with zipfile.ZipFile(archive_path) as archive:
    for item in archive.infolist():
        destination = (target / item.filename).resolve()
        if not destination.is_relative_to(target.resolve()):
            raise SystemExit('Invalid source ZIP path')
    if archive.testzip() is not None:
        raise SystemExit('Source ZIP integrity check failed')
    archive.extractall(target)
(target / 'app-version.txt').write_text(version + '\n', encoding='utf-8')
wrapper = target / 'gradlew'
if wrapper.exists():
    wrapper.chmod(wrapper.stat().st_mode | 0o111)
print('Source prepared at .build/project; version ' + version)
