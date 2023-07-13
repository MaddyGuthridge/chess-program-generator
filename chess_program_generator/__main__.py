from argparse import ArgumentParser
from .generator import generate


parser = ArgumentParser(
    'chess_program_generator',
    description='Generate a Python program for playing chess',
)


parser.add_argument('depth', action='store', type=int)


args = parser.parse_args()

depth: int = args.depth
generate(depth)
