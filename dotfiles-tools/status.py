from pathlib import Path
from os import path
from conf_parse import Config

def status(config: Config):
    found_error = check_if_src_exists(config)
    found_error = check_if_link_is_set(config) or found_error

    if found_error:
        exit(1)
    else:
        exit(0)


def check_if_link_is_set(config: Config):
    found_error = False
    for link in config.get_links():
        dest: Path = link.get_dest()
        if not dest.is_symlink():
            found_error = True
            print('File "' + dest.as_uri() + '" is not a symbolic link')
    return found_error


def check_if_src_exists(config: Config):
    found_error = False
    for link in config.get_links():
        if not path.exists(link.get_src()):
            found_error = True
            print('Could not find file: "' + link.get_src().as_uri() + '"')
    return found_error


