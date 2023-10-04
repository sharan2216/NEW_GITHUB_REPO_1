import pytest


@pytest.fixture(params=["a","b"])
def demo_fixture(request):
    print(request.param)


def test_login(demo_fixture):
    print("Login successful")


# def test_logoff():
#     print("Logoff successful")
#
# def test_calcilation():
#     assert 2+2==4



