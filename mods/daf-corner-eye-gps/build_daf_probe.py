"""Build the DAF XG+ Argenta GPS / CornerEye rendering probe."""
import argparse
import re
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile

INTERIOR = "def/vehicle/truck/daf.2021/interior/xg_plus_argenta.sii"
GPS = "ui/dashboard/daf_2021_gps.sii"
CORNER = "ui/dashboard/daf_2021_front_cam_mirror.sii"
PROBE = "ui/dashboard/xgplus_corner_probe.sii"


def build(source: Path, output: Path):
    interior = (source / INTERIOR).read_text(encoding="utf-8")
    corner = (source / CORNER).read_text(encoding="utf-8")
    old = f'gps_path: "/{GPS}"'
    if interior.count(old) != 1 or "front_mirror_reflection.mat" not in corner:
        raise ValueError("Unexpected DAF definitions. Check the extracted archive.")
    # Keep the factory drawable size. Stretch the original UI over its full viewport.
    corner = re.sub(r"((?:coords|area)_r: )(?:256|512)\b", r"\g<1>1280", corner)
    corner = re.sub(r"((?:coords|area)_t: )(?:128|768)\b", r"\g<1>720", corner)
    # GPS uses a basic screen. The donor's ID 1640 is a mirror accessory visibility gate.
    corner, count = re.subn(r"(id: )1640\b", r"\g<1>100", corner)
    if count != 1:
        raise ValueError("Expected one CornerEye visibility group.")
    manifest = """SiiNunit
{
mod_package : .package {
 package_version: "0.1"
 display_name: "DAF XG+ CornerEye GPS Probe"
 author: "XENO LUCUS"
 compatible_versions[]: "1.62.*"
}
}
"""
    output.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=output.parent) as temp:
        staged = Path(temp) / output.name
        with ZipFile(staged, "w", ZIP_DEFLATED) as archive:
            archive.writestr("manifest.sii", manifest)
            archive.writestr(INTERIOR, interior.replace(old, f'gps_path: "/{PROBE}"'))
            archive.writestr(PROBE, corner)
        staged.replace(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Extracted dlc_daf_2021.scs root")
    parser.add_argument("output", type=Path, help="Output .scs path")
    args = parser.parse_args()
    build(args.source, args.output)
