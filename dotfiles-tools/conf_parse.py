from pathlib import Path


class Link:
    def __init__(self, src: Path, dest: Path):
        self._src = src
        self._dest = dest

    def get_src(self) -> Path:
        return self._src

    def get_dest(self) -> Path:
        return self._dest


class Config:
    def __init__(self):
        self._links = []

    def add_link(self, link: Link):
        self._links.append(link)

    def get_links(self) -> [Link]:
        return self._links


def conf_parse(file: Path, src_dir: Path) -> Config:
    config = Config()
    f = open(file, "r")
    for line in f.readlines():
        parse_line(line, config, src_dir)
    f.close()
    return config


def parse_line(line: str, config: Config, src_dir: Path):
    split = line.strip().split(";")
    if len(split) != 2:
        print("Invalid line \"" + line + "\"")
        return
    src = src_dir / Path(split[0])
    dest = Path(split[1]).expanduser().absolute()
    config.add_link(Link(src, dest))

