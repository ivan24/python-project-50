import argparse


def gendiff_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='tests/fixtures/file1.json')
    parser.add_argument('second_file', help='tests/fixtures/file2.json')
    parser.add_argument('-f', '--format',
                        default='FORMAT',
                        help='set format of output')
    args = parser.parse_args()
    return args
