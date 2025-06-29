"""A module to bootstrap the rescreener application."""
import argparse
import sys

from fastapi import FastAPI

from rescreener.api import routes
from rescreener.utils.pyproject import PRG, DESCRIPTION, VERSION

__all__ = ['main']

def _parse_args(args: list) -> list:
    """Parse command line arguments."""
    # ---------- >>> parse CLI options <<< -------------------------------------
    parser = argparse.ArgumentParser(prog=PRG,
                                     description=DESCRIPTION)
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
    args = _parse_args(args)

    if args.debug:
        # TODO run FastAPI in debug mode
        print('running in debug mode')

    app = FastAPI()
    app.include_router(routes.router)

if __name__ == '__main__':
    main()
