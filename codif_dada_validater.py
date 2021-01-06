#!/usr/local/bin/python2.7


import json
import curses
import argparse
import os
import re
from argparse import RawTextHelpFormatter

from inc.codif import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='options', formatter_class=RawTextHelpFormatter)
    parser.add_argument('--fname', '-f', action = "store", default = "2020-12-03-22:48:30", dest = "fname", help = "Input file name with directory (filetype '.dada')")
    parser.add_argument('--dir', '-d', action = "store", default = "/beegfsEDD/NESSER/", dest = "dir", help = "Input file name with directory (filetype '.dada')")
    parser.add_argument('--packets', '-p', action = "store", default=-1, dest = "packets", help = "Packets to read from .dada file")
    parser.add_argument('--threads', '-t', action = "store", default=2, dest = "threads", help = "Packets to read from .dada file")
    parser.add_argument('--output', '-o', action = "store", default= "2020-12-03-22:48:30.csv", dest = "output", help = "Packets to read from .dada file")

    fname = parser.parse_args().fname
    dir = parser.parse_args().dir
    packets = int(parser.parse_args().packets)
    threads = int(parser.parse_args().threads)
    output = parser.parse_args().output
    file_list = []
    fname_list = []
    cnt = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            if fname in file:
                file_list.append(os.path.join(root, file))

    file_list.sort(key=splitter)
    handler = CodifHandler(file_list)
    handler.validate(packets, threads=threads, display="node")
    handler.to_csv("results/", output)
