import os
from pathlib import Path

from conf_parse import Config


def setup(config: Config):
    for link in config.get_links():
        src = link.get_src()
        dest: Path = link.get_dest()
        if dest.exists():
            print(dest.as_uri() + " exists")
            continue
        create_path(dest.parent)
        os.symlink(src, dest)
    exit(0)


def create_path(dest: Path):
    if not dest.exists():
        os.makedirs(dest)
