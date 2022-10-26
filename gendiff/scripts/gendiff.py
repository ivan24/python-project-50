#!/usr/bin/env python3
from gendiff.cli import gendiff_parser
from gendiff.file_diff import generate_diff


def main():
    args = gendiff_parser()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == 'main':
    main()
