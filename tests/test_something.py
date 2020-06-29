import pytest


def setup_function(function):
    print("setting up", function)


def test_import():
    from sphinxcontrib import vhdldomain
    print(vhdldomain)


def test_something():
    from sphinxcontrib import vhdldomain  # noqa F401
    print("idk")


if __name__ == '__main__':
    pytest.main([__file__])
