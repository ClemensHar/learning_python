import pytest


@pytest.mark.skip
def testLogin():
    print("Login Successful")


def testLogoff():
    print("Logoff Successful")


@pytest.mark.sanity
def testCalculation():
    assert 2 + 2 == 4


@pytest.mark.xfail  # mark this test as an expected failure (e.g. if function to be tested has not been defined yet)
def testCalculation1():
    assert 2 + 2 == 5


print("This script ran")
