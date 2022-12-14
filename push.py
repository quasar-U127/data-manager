import argparse
import config
import os


def push_parser(parser: argparse.ArgumentParser):
    parser.add_argument(
        "path", type=str, help="Section of the data to be pushed to remote")
    parser.add_argument(
        "--info", action="store_true", help="get transfer progress")


def push(args: argparse.Namespace):
    conf = config.Config(args.root)
    if not conf.pushable():
        return
    remote = conf.remote()
    local = os.path.abspath(args.root)
    res = os.path.join(local, ".", args.path)
    info = ""
    if args.info:
        info = "--info=progress2"
    os.system(f"rsync -avz {info} --relative \"{res}\" \"{remote}\"")
