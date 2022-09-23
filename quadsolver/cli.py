import argparse


def parse_args():
    """Parse command line arguments

    :return args: arguments as an `args.Namespace` object
    :rtype args: args.Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'coefficients',
        type=float,
        nargs=3,
        help="coefficients for a, b, and c (in order)"
    )

    parser.add_argument('-v', '--verbose', action='store_true', help="verbose output [default: False]")
    parser.add_argument('-o', '--output', help="a file to write to [default: stdout]")
    parser.add_argument('--overwrite', action='store_true', help="overwrite the current file [default: False]")
    args = parser.parse_args()
    return args
