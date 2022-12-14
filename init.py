import argparse
import os
import config


def init_parser(parser: argparse.ArgumentParser):
    pass


def init(args: argparse.Namespace):
    config.Config.save_empty(args=args)
