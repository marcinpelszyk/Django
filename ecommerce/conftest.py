import pytest



@pytest.fixture(scope='module')
def test_fixture1():
    print('Run once')
    return 1

    