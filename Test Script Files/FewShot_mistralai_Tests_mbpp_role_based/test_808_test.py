import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):
    def test_found_in_list(self):
        self.assertTrue(check_K([1, 2, 3, 4, 5], 3))

    def test_not_found_in_list(self):
        self.assertFalse(check_K([1, 2, 3, 4, 5], 6))

    def test_empty_list(self):
        self.assertFalse(check_K([]))

    def test_single_element_list(self):
        self.assertTrue(check_K([1]))

    def test_list_with_duplicates(self):
        self.assertTrue(check_K([1, 1, 2, 3, 4, 5], 1))
