import unittest
from mbpp_19_code import test_duplicate

class TestTestDuplicate(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(test_duplicate([1, 2, 3, 4, 5]))

    def test_duplicate_exists(self):
        self.assertTrue(test_duplicate([1, 2, 2, 3, 4]))

    def test_no_duplicate(self):
        self.assertFalse(test_duplicate([1, 2, 3, 4, 5]))

    def test_empty_list(self):
        self.assertFalse(test_duplicate([]))

    def test_single_element(self):
        self.assertFalse(test_duplicate([1]))

    def test_negative_numbers(self):
        self.assertTrue(test_duplicate([-1, -2, -2, -3]))

    def test_zero(self):
        self.assertTrue(test_duplicate([0, 0]))

    def test_large_numbers(self):
        self.assertTrue(test_duplicate([1000000, 2000000, 2000000]))

    def test_non_integer_elements(self):
        self.assertTrue(test_duplicate(['a', 'b', 'b']))
