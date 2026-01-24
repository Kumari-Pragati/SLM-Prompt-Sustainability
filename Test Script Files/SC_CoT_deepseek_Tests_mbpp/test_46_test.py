import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(test_distinct([1, 2, 3, 4, 5]))

    def test_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_single_element(self):
        self.assertTrue(test_distinct([1]))

    def test_duplicate_elements(self):
        self.assertFalse(test_distinct([1, 2, 2, 3, 4]))

    def test_large_list(self):
        self.assertTrue(test_distinct(list(range(1, 10001))))

    def test_large_duplicate_list(self):
        self.assertFalse(test_distinct([i for i in range(1, 10001) for _ in range(2)]))

    def test_negative_numbers(self):
        self.assertTrue(test_distinct([-1, -2, -3, -4, -5]))

    def test_negative_duplicate_numbers(self):
        self.assertFalse(test_distinct([-1, -2, -2, -3, -4]))

    def test_mixed_numbers(self):
        self.assertTrue(test_distinct([-1, 0, 1]))

    def test_mixed_duplicate_numbers(self):
        self.assertFalse(test_distinct([-1, 0, 0, 1]))

    def test_non_integer_elements(self):
        self.assertTrue(test_distinct([1.0, 2.0, 3.0, 4.0, 5.0]))

    def test_non_integer_duplicate_elements(self):
        self.assertFalse(test_distinct([1.0, 2.0, 2.0, 3.0, 4.0]))
