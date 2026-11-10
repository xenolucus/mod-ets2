"""Build the ETS2 1.62 test-profile economy mod from extracted def.scs."""
import argparse
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

CHANGES = {
    "def/economy_data.sii": {
        "price_small_garage": "1",
        "price_garage_upgrade": "1",
        "truck_count_for_online": "1",
        "fixed_revenue": "1000000",
        "exp_cargo_delivery": "1000.0",
        "exp_park_bonus": "150000",
        "exp_park_bonus_medium": "150000",
        "exp_park_bonus_hard": "150000",
    },
    "def/initial_save/normal/game.sii": {"money_account": "100000000"},
}

MANIFEST = """SiiNunit
{
mod_package : .package {
 package_version: "0.1"
 display_name: "ETS2 Test Fleet Bootstrap"
 author: "XENO LUCUS"
 compatible_versions[]: "1.62.*"
}
}
"""


def build(source: Path, output: Path):
    files = {"manifest.sii": MANIFEST}
    for relative, changes in CHANGES.items():
        content = (source / relative).read_text(encoding="utf-8")
        for key, value in changes.items():
            pattern = rf"(?m)^([ \t]*{re.escape(key)}:[ \t]*)[^\s#]+"
            content, count = re.subn(pattern, lambda match: match[1] + value, content)
            if count != 1:
                raise ValueError(f"{relative}: expected one {key}, found {count}")
        files[relative] = content

    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for relative, content in files.items():
            archive.writestr(relative, content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Extracted def.scs root")
    parser.add_argument("output", type=Path, help="Output .scs path")
    args = parser.parse_args()
    build(args.source, args.output)
