import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_single_element_list(self):
        self.assertTrue(test_distinct([1]))

    def test_distinct_elements(self):
        self.assertTrue(test_distinct([1, 2, 3, 4, 5]))

    def test_non_distinct_elements(self):
        self.assertFalse(test_distinct([1, 1, 2, 2, 3, 3]))

    def test_distinct_elements_with_duplicates(self):
        self.assertTrue(test_distinct([1, 2, 2, 3, 4, 5]))

    def test_empty_set(self):
        self.assertTrue(test_distinct({}))

    def test_single_element_set(self):
        self.assertTrue(test_distinct({1}))

    def test_distinct_elements_set(self):
        self.assertTrue(test_distinct({1, 2, 3, 4, 5}))

    def test_non_distinct_elements_set(self):
        self.assertFalse(test_distinct({1, 1, 2, 2, 3, 3}))

    def test_distinct_elements_set_with_duplicates(self):
        self.assertTrue(test_distinct({1, 2, 2, 3, 4, 5}))
