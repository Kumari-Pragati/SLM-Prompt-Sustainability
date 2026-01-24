import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(test_distinct([1, 2, 3, 4, 5]))

    def test_typical_case_with_duplicates(self):
        self.assertFalse(test_distinct([1, 2, 2, 3, 4]))

    def test_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_single_element_list(self):
        self.assertTrue(test_distinct([1]))

    def test_all_duplicates(self):
        self.assertFalse(test_distinct([1, 1, 1, 1]))

    def test_large_list(self):
        self.assertTrue(test_distinct(list(range(1, 1001))))

    def test_large_list_with_duplicates(self):
        self.assertFalse(test_distinct(list(range(1, 1001)) + [1001]))
