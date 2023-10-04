import pytest


@pytest.fixture(scope="session" ,autouse=True)
def setup():
    print("launch Browser")
    print("Login")
    print("Browse Products")
    yield
    print("LOGOFF")
    print("CLOSE BROWSER")
