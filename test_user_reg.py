import pytest
from user_registration import UserRegistration


@pytest.fixture
def user_obj_t():
    return UserRegistration("Omkar", "Bhise", "omkarbhise8745@gmail.com", "91 6235236988")


@pytest.fixture
def user_obj_f():
    return UserRegistration("omkar", "nj", "adadfa@adf", "91 5623412323")


def test_first_name_success(user_obj_t, user_obj_f):
    assert user_obj_t.check_first_name() is True
    assert user_obj_f.check_first_name() is False


def test_last_name_success(user_obj_t, user_obj_f):
    assert user_obj_t.check_last_name() is True
    assert user_obj_f.check_last_name() is False


def test_mobile_num(user_obj_t, user_obj_f):
    assert user_obj_t.check_mobile_num() is True
    assert user_obj_f.check_mobile_num() is False


def test_check_email(user_obj_f, user_obj_t):
    assert user_obj_t.check_email() is True
    assert user_obj_f.check_email() is False
