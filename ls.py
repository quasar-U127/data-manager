import argparse

def ls_parser(parser:argparse.ArgumentParser):
    parser.add_argument("path",type=str,help="Section of the data to be ls'd from local")

def ls_remote_parser(parser:argparse.ArgumentParser):
    parser.add_argument("path",type=str,help="Section of the data to be ls'd from remote")