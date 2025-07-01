"""A module to bootstrap the rescreener application."""

import argparse
import sys

import uvicorn
from fastapi import FastAPI

from rescreener.api import routes
from rescreener.utils.pyproject_utils import PRG, DESCRIPTION, VERSION

__all__ = ['app', 'main']

app = FastAPI()
app.include_router(routes.router)


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
    args = parser.parse_args(args)
    return args


# ------------------------------------------------------------------------------
# --------------->>> start <<<---------------------------------------------------
# ------------------------------------------------------------------------------
def main(args=sys.argv[1:]) -> None:
    """The application bootstrap main function."""
    args = _parse_args(args)

    # only run if block when NOT running unit test
    if 'unittest' not in sys.modules:
        if args.debug:
            uvicorn.run(app, host="127.0.0.1", port=8080)


if __name__ == '__main__':
    main()
