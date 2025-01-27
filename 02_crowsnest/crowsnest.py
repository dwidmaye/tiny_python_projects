#!/usr/bin/env python3
"""
Author : Derek Widmayer <dwidmaye@gmail.com>
Date   : 2021-01-04
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- Choose the correct article.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')
    parser.add_argument('-s', '--side',
                        metavar='side',
                        help='larboard or sideboard',
                        default='larboard')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = args.side
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    article = article.title() if word.istitle() else article
    print(f'Ahoy, Captain, {article} {word} off the {side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
