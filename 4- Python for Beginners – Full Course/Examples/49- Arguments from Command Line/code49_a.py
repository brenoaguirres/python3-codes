# Arguments CLI

import argparse

# the built-in argparse module will help with validating arguments passed via CLI
parser = argparse.ArgumentParser(
    description='This program prints the name of my dogs'
)

parser.add_argument('-c', '--color', metavar='color',
                    required=True, choices={'red', 'yellow', 'black'},
                    help='the color to search for')

args = parser.parse_args()

print(args.color)

