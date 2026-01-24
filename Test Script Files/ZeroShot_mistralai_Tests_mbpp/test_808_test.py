import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(check_K([], 1))

    def test_single_element(self):
        self.assertTrue(check_K([1], 1))
        self.assertFalse(check_K([1], 2))

    def test_multiple_elements(self):
        self.assertTrue(check_K([1, 1], 1))
        self.assertFalse(check_K([1, 1], 2))
        self.assertTrue(check_K([2, 1], 1))
        self.assertFalse(check_K([2, 1], 2))
