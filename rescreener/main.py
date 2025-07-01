"""A module to bootstrap the rescreener application."""

import argparse
import sys
from argparse import ArgumentParser
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from rescreener.api import routes
from rescreener.config import Settings
from rescreener.utils.file_utils import get_root_dir
from rescreener.utils.pyproject_utils import PRG, DESCRIPTION, VERSION

__all__ = ['app', 'main']

settings = Settings()

app = FastAPI()

static_path: Path = Path(get_root_dir() / "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")
app.include_router(routes.router)


def _setup_parser() -> ArgumentParser:
    """Initialize parser with additional CLI options."""
    parser: ArgumentParser = argparse.ArgumentParser(prog=PRG,
                                                     description=DESCRIPTION)
    # ---------- >>> Add CLI options <<< --------------------------------------
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help='run application in debug mode')
    parser.add_argument('-V', '--version',
                        action='version',
                        help='display version information',
                        version='%(prog)s ' + VERSION)
    return parser


# -----------------------------------------------------------------------------
# --------------->>> start <<<-------------------------------------------------
# NOTE: main() is NOT called when executing program using "fastapi" executor.
# -----------------------------------------------------------------------------
def main(argv: list[str] = sys.argv[1:]) -> None:
    """The application bootstrap main function."""
    parser: ArgumentParser = _setup_parser()
    # process the input argv: could exit the application.
    args: list[str] = parser.parse_args(argv)

    if args is not None:
        print(f"Starting {PRG} with the following CLI options:", args)

    # skip running application when unit testing
    if 'unittest' in sys.modules:
        print(f"Skipping {PRG} application startup in unit test mode.")
        return None

    # start the application
    return uvicorn.run(app, host=settings.host, port=settings.port)


if __name__ == '__main__':
    sys.exit(main())
