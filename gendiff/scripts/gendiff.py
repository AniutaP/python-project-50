#!/usr/bin/env python3
from gendiff.parse_args import make_parse_args
from gendiff import generate_diff


def main():
    args = make_parse_args()
    first_file = args.first_file
    second_file = args.second_file
    formatter = args.format
    result = generate_diff(first_file, second_file, formatter)
    print(result)


if __name__ == '__main__':
    main()
