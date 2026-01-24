import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(all_unique([]))

    def test_single_element_list(self):
        self.assertTrue(all_unique([1]))

    def test_duplicate_elements_list(self):
        self.assertFalse(all_unique([1, 1]))

    def test_unique_elements_list(self):
        self.assertTrue(all_unique([1, 2, 3]))

    def test_large_unique_list(self):
        self.assertTrue(all_unique(list(range(100))))

    def test_large_duplicate_list(self):
        self.assertFalse(all_unique(list(range(10)) * 2))
