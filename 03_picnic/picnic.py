#!/usr/bin/env python3
"""
Author : Derek Widmayer <dwidmaye@gmail.com>
Date   : 2021-01-05
Purpose: Rock the Casbah
"""

import argparse

template = "You are bringing {}."


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='List picnic items to bring.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Picnic Game."""

    args = get_args()
    item = args.item
    if args.sorted:
        item.sort()
    items = ""

    if len(item) == 1:
        items = ''.join(item)
    elif len(item) == 2:
        items = ' and '.join(item)
    else:
        last_item = item.pop()
        items = ', '.join(item) + ', and ' + last_item

    print(template.format(items))


# --------------------------------------------------
if __name__ == '__main__':
    main()
