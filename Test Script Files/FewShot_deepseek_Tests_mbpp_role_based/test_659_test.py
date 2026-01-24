import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Repeat([1, 2, 2, 3, 4, 4, 4, 5, 5]), [2, 4, 5])

    def test_empty_list(self):
        self.assertEqual(Repeat([]), [])

    def test_list_with_single_element(self):
        self.assertEqual(Repeat([1]), [])

    def test_list_with_repeated_elements(self):
        self.assertEqual(Repeat([1, 1, 1, 1]), [1])

    def test_list_with_all_same_elements(self):
        self.assertEqual(Repeat([1, 1, 1, 1, 1]), [1])

    def test_list_with_no_repeated_elements(self):
        self.assertEqual(Repeat([1, 2, 3, 4, 5]), [])
