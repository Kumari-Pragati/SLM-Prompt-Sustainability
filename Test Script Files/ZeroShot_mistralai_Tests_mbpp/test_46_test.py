import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_single_element(self):
        self.assertTrue(test_distinct([1]))

    def test_duplicates(self):
        self.assertFalse(test_distinct([1, 1]))

    def test_multiple_elements(self):
        self.assertTrue(test_distinct([1, 2, 3]))

    def test_mixed_data_types(self):
        self.assertFalse(test_distinct([1, 'a', 2, 'a']))

    def test_list_with_none(self):
        self.assertTrue(test_distinct([None]))

    def test_list_with_multiple_none(self):
        self.assertTrue(test_distinct([None, None, 1]))
