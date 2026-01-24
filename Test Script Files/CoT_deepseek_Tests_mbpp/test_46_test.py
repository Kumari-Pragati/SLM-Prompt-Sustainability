import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(test_distinct([1, 2, 3, 4, 5]))

    def test_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_duplicate_elements(self):
        self.assertFalse(test_distinct([1, 2, 2, 3, 4]))

    def test_single_element(self):
        self.assertTrue(test_distinct([1]))

    def test_large_list(self):
        self.assertTrue(test_distinct(list(range(1, 1001))))

    def test_large_duplicate_list(self):
        self.assertFalse(test_distinct([1] * 1001))

    def test_negative_numbers(self):
        self.assertTrue(test_distinct([-1, -2, -3, -4, -5]))

    def test_mixed_numbers(self):
        self.assertTrue(test_distinct([-1, 0, 1]))
