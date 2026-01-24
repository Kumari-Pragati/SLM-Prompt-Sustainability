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
        self.assertFalse(test_distinct([1, 1, 1]))

    def test_large_distinct_list(self):
        self.assertTrue(test_distinct(list(range(1, 10001))))

    def test_large_duplicate_list(self):
        self.assertFalse(test_distinct([1] * 10001))
