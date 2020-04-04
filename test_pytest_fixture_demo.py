import pytest


@pytest.fixture()
def setup():
    print("this gets executed before any method that calls this method")

def test_method_1(setup):
    print("this is in method 1")

def test_method_2(setup):
    print("this is in method 2")
    