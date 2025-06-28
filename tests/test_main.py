import argparse
from rescreener.main import main, main_parse_args

def test_main_parse_args():
    argv = ['--testing']
    args = main_parse_args(argv)
    assert isinstance(args, argparse.Namespace)

def test_main():
    argv = ['--testing']
    main(argv)
    # ensure we get this far
    assert True
