import pytest


@pytest.fixture(scope="session", autouse=True)
def tc_setup():
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield  # statements beyond the yield, will be performed after the test -> teardown
    print("Logoff")
    print("Close browser")
