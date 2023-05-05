#!usr/bin/env python3
import argparse
from gendiff.gendiff_parser import generate_gendiff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default="stylish",
        choices=['flat', 'stylish'],
        help='set format of output'
    )
    args = parser.parse_args()

    print(generate_gendiff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
