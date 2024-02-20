from utils import arrs
import pytest


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(["none"], 999, "test") == "test"
    assert arrs.get([1, 2, 3], 0, "test") == 1



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3) == [3, 4, 5]
    assert arrs.my_slice([6, 7, 8, 9], 3) == [9]
    assert arrs.my_slice([], -3) == []
    assert arrs.my_slice([0], None, 0) == []
