import pytest

#########################################################
# using pytest.yield_fixture() and yield in setup method allows the pytest to #
# execute the setup method before and after the calling method executed.
##########################################################


# This is a python decarator having special purpose in pytest to allow DRY
@pytest.yield_fixture()
def setup():
    print("this gets executed before any method that calls this method")
    yield
    print("This setup method is executed after the calling method is executed ")

def test_method_1(setup):
    print("this is in method 1")

def test_method_2(setup):
    print("this is in method 2")