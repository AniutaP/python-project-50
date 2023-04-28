#!/usr/bin/env python3
import argparse


def make_parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=open)
    parser.add_argument('second_file', type=open)
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()
