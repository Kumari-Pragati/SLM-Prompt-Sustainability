import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(Repeat([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(Repeat([1, 2, 2, 3, 4, 4, 5]), [2, 4])

    def test_empty_list(self):
        self.assertEqual(Repeat([]), [])

    def test_list_with_duplicates(self):
        self.assertEqual(Repeat([1, 1, 2, 2, 3, 3, 4, 4, 5]), [1, 2, 3, 4])

    def test_list_with_no_duplicates(self):
        self.assertEqual(Repeat([1, 2, 3, 4, 5]), [])

    def test_list_with_duplicates_and_non_duplicates(self):
        self.assertEqual(Repeat([1, 1, 2, 3, 4, 5, 5, 6]), [1, 2, 5])
