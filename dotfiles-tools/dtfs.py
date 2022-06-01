#!env/bin/python3
import argparse
import os
from pathlib import Path

import conf_parse
from setup import setup
from status import status


def main():
    main_dir = Path(os.path.dirname(__file__)).parent.absolute()
    config_file = main_dir / "config"
    dot_files = main_dir / "files"
    config = conf_parse.conf_parse(config_file, dot_files)
    args = read_args()
    if args.command == "setup":
        setup(config)
    elif args.command == "status":
        status(config)


def read_args():
    parser = argparse.ArgumentParser(description="A tool for my dotfiles")
    setup_args = sub_parsers = parser.add_subparsers(dest="command", required=True)
    setup_args.add_parser("--symlink")
    sub_parsers.add_parser("setup", help="Link files using symbolic links")
    sub_parsers.add_parser("status", help="Check configuration")
    return parser.parse_args()


if __name__ == '__main__':
    main()
