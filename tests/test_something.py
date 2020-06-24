import pytest


def test_import():
    from sphinxcontrib import vhdldomain
    print(vhdldomain)



if __name__ == '__main__':
    pytest.main([__file__])
