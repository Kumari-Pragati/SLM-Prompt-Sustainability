import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):

    def test_true(self):
        self.assertTrue(check_K((1, 2, 3, 4), 3))

    def test_false(self):
        self.assertFalse(check_K((1, 2, 3, 4), 5))

    def test_first_match(self):
        self.assertTrue(check_K((1, 2, 3, 4), 1))

    def test_last_match(self):
        self.assertTrue(check_K((1, 2, 3, 4), 4))

    def test_middle_match(self):
        self.assertTrue(check_K((1, 2, 3, 4), 3))

    def test_empty_tuple(self):
        self.assertFalse(check_K((), 1))

    def test_single_element_tuple(self):
        self.assertFalse(check_K((1,), 2))

    def test_single_match(self):
        self.assertTrue(check_K((1, 2, 3, 4), 2))

    def test_no_match(self):
        self.assertFalse(check_K((1, 2, 3, 4), 6))
