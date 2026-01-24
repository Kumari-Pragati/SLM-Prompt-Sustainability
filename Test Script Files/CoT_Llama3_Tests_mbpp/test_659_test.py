import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Repeat([]), [])

    def test_single_element_list(self):
        self.assertEqual(Repeat([1]), [])

    def test_no_repeated_elements(self):
        self.assertEqual(Repeat([1, 2, 3, 4, 5]), [])

    def test_repeated_elements(self):
        self.assertEqual(Repeat([1, 2, 2, 3, 4, 4, 5]), [2, 4])

    def test_repeated_elements_with_duplicates(self):
        self.assertEqual(Repeat([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]), [2, 3, 4])

    def test_repeated_elements_with_duplicates_and_order(self):
        self.assertEqual(Repeat([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), [2, 3, 4, 5])

    def test_repeated_elements_with_duplicates_and_order_and_duplicates(self):
        self.assertEqual(Repeat([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5]), [2, 3, 4, 5])
