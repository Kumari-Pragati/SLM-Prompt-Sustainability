import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):

    def test_distinct_with_distinct_elements(self):
        self.assertTrue(test_distinct([1, 2, 3, 4, 5]))

    def test_distinct_with_duplicate_elements(self):
        self.assertFalse(test_distinct([1, 2, 2, 3, 4]))

    def test_distinct_with_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_distinct_with_single_element(self):
        self.assertTrue(test_distinct([1]))
