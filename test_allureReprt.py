import pytest


def first_scenario():
    a = 5
    b = 6
    assert a == b


def second_scenario():
    a = 5
    b = 6
    assert a*b == b*a


def third_scenario():
    a = 5
    b = 6
    assert a-b == b-a