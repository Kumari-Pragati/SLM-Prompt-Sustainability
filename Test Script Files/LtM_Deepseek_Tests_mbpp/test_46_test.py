import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertTrue(test_distinct([1, 2, 3, 4, 5]))

    def test_empty_input(self):
        self.assertTrue(test_distinct([]))

    def test_duplicate_elements(self):
        self.assertFalse(test_distinct([1, 2, 2, 3, 4]))

    def test_single_element(self):
        self.assertTrue(test_distinct([1]))

    def test_large_set_with_duplicates(self):
        self.assertFalse(test_distinct(list(range(1, 10001)) + [10001]))
