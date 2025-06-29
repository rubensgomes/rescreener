"""rescreener bootstrap main module"""
import argparse
import sys

from rescreener.utils.pyproject import PRG, DESCRIPTION, VERSION

# ------------------------------------------------------------------------------
# --------------->>> parse_args <<<---------------------------------------------
# ------------------------------------------------------------------------------
def main_parse_args(args: list) -> list:
    """Parse command line arguments."""
    # ---------- >>> parse CLI options <<< -------------------------------------
    parser = argparse.ArgumentParser(prog=PRG,
                                     description=DESCRIPTION)
    parser.add_argument('-t', '--testing',
                        action='store_true',
                        help='run application in testing mode')
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help='run application in debug mode')
    parser.add_argument('-V', '--version',
                        action='version',
                        help='display version information',
                        version='%(prog)s ' + VERSION)
    # reads default args from sys.argv
    return parser.parse_args(args)

# ------------------------------------------------------------------------------
# --------------->>> start <<<---------------------------------------------------
# ------------------------------------------------------------------------------
def main(args=sys.argv[1:]) -> None:
    """The application bootstrap main function."""
    args = main_parse_args(args)
    print("Hello World")

if __name__ == '__main__':
    main()
