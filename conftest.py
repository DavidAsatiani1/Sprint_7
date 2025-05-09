import pytest
from helpers import *


@pytest.fixture(scope='function')
def create_courier():
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass