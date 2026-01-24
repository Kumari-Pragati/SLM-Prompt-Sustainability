import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5), 3))

    def test_false(self):
        self.assertFalse(check_K((1, 2, 3, 4, 5), 6))

    def test_first_element(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5), 1))

    def test_last_element(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5), 5))

    def test_middle_element(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5), 3))

    def test_empty_tuple(self):
        self.assertFalse(check_K((), 1))

    def test_single_element(self):
        self.assertTrue(check_K((1,), 1))

    def test_no_element(self):
        self.assertFalse(check_K((1, 2, 3, 4), 5))
