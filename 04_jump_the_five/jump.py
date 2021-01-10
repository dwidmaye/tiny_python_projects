#!/usr/bin/env python3
"""
Author : Derek Widmayer <dwidmaye@gmail.com>
Date   : 2021-01-10
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Jump the five"""

    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Encode jump the five"""

    text = get_args().str
    encoding = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0', '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    encoded_text = ""
    for char in text:
        encoded_text += encoding.get(char, char)

    print(f'{encoded_text}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
