import argparse
import os
import config


def pull_parser(parser: argparse.ArgumentParser):
    parser.add_argument(
        "path", type=str, help="Section of the data to be pulled from remote")
    parser.add_argument(
        "--info", action="store_true", help="get transfer progress")


def pull(args: argparse.Namespace):
    conf = config.Config(args.root)
    remote = conf.remote()
    local = os.path.abspath(args.root)
    res = os.path.join(remote, ".", args.path)
    info = ""
    if args.info:
        info = "--info=progress2"
    os.system(f"rsync -avz {info} --relative \"{res}\" \"{local}\"")
