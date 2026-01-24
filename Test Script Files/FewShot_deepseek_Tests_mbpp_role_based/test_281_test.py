import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(all_unique([1, 2, 3, 4]))

    def test_typical_use_case_with_duplicates(self):
        self.assertFalse(all_unique([1, 2, 2, 3, 4]))

    def test_empty_list(self):
        self.assertTrue(all_unique([]))

    def test_single_element_list(self):
        self.assertTrue(all_unique([1]))

    def test_large_list_with_duplicates(self):
        self.assertFalse(all_unique(list(range(1000)) + [1]))

    def test_large_list_without_duplicates(self):
        self.assertTrue(all_unique(list(range(1000))))

    def test_list_with_non_integer_elements(self):
        self.assertFalse(all_unique(['a', 'b', 'b', 'c']))
