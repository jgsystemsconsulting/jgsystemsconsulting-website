"""Assert the academic form consent gate. Stdlib only. Run from repo root."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACADEMIC = ROOT / "docs" / "academic.html"
EULA = ROOT / "docs" / "eula.html"


def fail(msg):
    print("FAIL:", msg, file=sys.stderr)
    sys.exit(1)


def main():
    if not ACADEMIC.is_file():
        fail("missing %s" % ACADEMIC)
    text = ACADEMIC.read_text(encoding="utf-8")
    box = re.search(
        r'<input\b(?=[^>]*\btype="checkbox")(?=[^>]*\bname="eula_accept")'
        r'(?=[^>]*\bvalue="accepted")(?=[^>]*\brequired\b)[^>]*>',
        text,
    )
    if not box:
        fail("academic form missing required eula_accept checkbox")
    hidden = re.search(
        r'<input\b(?=[^>]*\btype="hidden")(?=[^>]*\bname="eula_version")'
        r'(?=[^>]*\bvalue="(\d{4}-\d{2})")[^>]*>',
        text,
    )
    if not hidden:
        fail("academic form missing hidden eula_version YYYY-MM")
    version = hidden.group(1)
    label = re.search(
        r'<label\b[^>]*\bfor="eula_accept"[^>]*>.*?</label>',
        text,
        re.DOTALL,
    )
    if not label:
        fail("missing label for eula_accept")
    if 'href="eula.html"' not in label.group(0):
        fail("eula_accept label does not link eula.html")
    if 'target="_blank"' not in label.group(0):
        fail("eula_accept label link missing target=_blank")
    if version not in label.group(0):
        fail("label version %r does not match hidden eula_version" % version)
    if not EULA.is_file():
        fail("missing %s" % EULA)
    eula = EULA.read_text(encoding="utf-8")
    if version not in eula:
        fail("eula.html does not contain version %s" % version)
    if "DOC-ID: JGSC-WEB-004" not in eula:
        fail("eula.html missing DOC-ID JGSC-WEB-004")
    print("ok eula_version=%s" % version)


if __name__ == "__main__":
    main()
