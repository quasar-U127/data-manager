import argparse
import os
import config


def clone_parser(parser: argparse.ArgumentParser):
    parser.add_argument(
        "repo", type=str, help="Location of repo in the server of ada for eg ada:<some place>")
    parser.add_argument(
        "--info", action="store_true", help="get transfer progress")


def clone(args: argparse.Namespace):

    remote = args.repo
    _, repo_name = os.path.split(remote)
    local = os.path.abspath(args.root)
    # local = args.root
    local = os.path.join(local, repo_name)
    os.makedirs(local, exist_ok=False)
    info = ""
    if args.info:
        info = "--info=progress2"
    os.system(f"rsync -avz {info} --relative \"{remote}/./.data-config\" \"{local}\"")
