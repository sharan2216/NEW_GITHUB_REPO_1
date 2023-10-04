import pytest

# some lines added 1
# some lines added 2
# some lines added 3
# some lines added 4
# some lines added 5


def test_login():
    print("Login successful")


@pytest.mark.regression
def test_logoff():
    print("Logoff successful")


@pytest.mark.sanity
def test_calcilation():
    assert 2 + 2 == 4
