import unittest
from mbpp_899_code import check

class TestCheck(unittest.TestCase):
    def test_positive_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(check(arr, len(arr)))

    def test_negative_array(self):
        arr = [5, 4, 3, 2, 1]
        self.assertFalse(check(arr, len(arr)))

    def test_flat_array(self):
        arr = [1, 1, 1, 1, 1]
        self.assertTrue(check(arr, len(arr)))

    def test_array_with_one_element(self):
        arr = [1]
        self.assertTrue(check(arr, len(arr)))

    def test_array_with_two_elements(self):
        arr = [1, 1]
        self.assertTrue(check(arr, len(arr)))

    def test_array_with_negative_elements(self):
        arr = [1, -1, 1, -1, 1]
        self.assertFalse(check(arr, len(arr)))

    def test_array_with_zero_elements(self):
        arr = [0, 0, 0, 0, 0]
        self.assertTrue(check(arr, len(arr)))
