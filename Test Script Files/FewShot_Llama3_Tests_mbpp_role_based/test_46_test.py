import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_single_element_list(self):
        self.assertTrue(test_distinct([1]))

    def test_duplicates(self):
        self.assertFalse(test_distinct([1, 1, 2, 2]))

    def test_no_duplicates(self):
        self.assertTrue(test_distinct([1, 2, 3, 4]))

    def test_large_list(self):
        data = [i for i in range(100)]
        self.assertTrue(test_distinct(data))

    def test_large_list_with_duplicates(self):
        data = [i for i in range(100)]
        data.extend(data)
        self.assertFalse(test_distinct(data))
