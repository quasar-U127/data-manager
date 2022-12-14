from argparse import Namespace
import argparse
import json
import os


class Config(object):
    config_name = ".data-config"
    fields = ["remote","push"]
    def __init__(self, root) -> None:
        self.conf_path = os.path.join(root, Config.config_name)
        with open(self.conf_path, "rb") as config_file:
            self.conf = json.load(config_file)

    def save_empty(args):
        conf = {}
        with open(os.path.join(args.root, Config.config_name), "w") as f:
            json.dump(conf, f)

    def save(self):
        with open(self.conf_path, "w") as config_file:
            json.dump(self.conf, config_file)

    def pushable(self) -> bool:
        if "push" in self.conf.keys() and self.conf["push"] == "0":
            return False
        else:
            return True

    def set_config(self, key, value):
        self.conf[key]=value

    def get_config(self, key):
        return self.conf[key]

    def remote(self) -> str:
        return self.conf["remote"]

def set_parser(parser: argparse.ArgumentParser):
    parser.add_argument("key",type=str,choices=Config.fields)
    parser.add_argument("value",type=str)


def get_parser(parser: argparse.ArgumentParser):
    parser.add_argument("key",type=str,choices=Config.fields)

def set_config(args:Namespace):
    conf = Config(args.root)
    conf.set_config(key=args.key,value=args.value)
    conf.save()

def get_config(args:Namespace):
    conf = Config(args.root)
    print(conf.get_config(key=args.key))

