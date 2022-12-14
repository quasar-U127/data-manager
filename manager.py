#!/usr/bin/env python

import argparse
import os
from clone import clone, clone_parser
from config import get_config, get_parser, set_config, set_parser
from init import init, init_parser
from ls import ls_parser, ls_remote_parser

from pull import pull, pull_parser
from push import push, push_parser


def main():
    parser = argparse.ArgumentParser(prog="Data Manager")
    parser.add_argument("--root", type=str, default=".")
    subparsers = parser.add_subparsers(dest="operation",required=True)
    pull_parser(subparsers.add_parser("pull"))
    push_parser(subparsers.add_parser("push"))
    ls_parser(subparsers.add_parser("ls"))
    ls_remote_parser(subparsers.add_parser("ls-remote"))
    clone_parser(subparsers.add_parser("clone"))
    init_parser(subparsers.add_parser("init"))
    set_parser(subparsers.add_parser("set"))
    get_parser(subparsers.add_parser("get"))
    args = parser.parse_args()

    operations = {
        "pull":pull,
        "push":push,
        # "ls":ls,
        # "ls-remote":ls-remote,
        "clone":clone,
        "init":init,
        "set":set_config,
        "get":get_config
    }
    operations[args.operation](args)
    

# if __name__ == "main":
# print("jkhdf")
main()