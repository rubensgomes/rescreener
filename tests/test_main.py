from rescreener.main import main

def test_main():
    argv = ['--debug']
    main(argv)
    # ensure we get this far
    assert True
