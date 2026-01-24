import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Repeat([]), [])

    def test_single_element_list(self):
        self.assertEqual(Repeat([1]), [])

    def test_no_duplicates_list(self):
        self.assertEqual(Repeat([1, 2, 3]), [])

    def test_duplicates_list(self):
        self.assertEqual(Repeat([1, 2, 1]), [1])

    def test_duplicates_list_with_order(self):
        self.assertEqual(Repeat([1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_list_with_order_and_length(self):
        self.assertEqual(Repeat([1, 2, 3, 1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_list_with_order_and_length_and_duplicates(self):
        self.assertEqual(Repeat([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_list_with_order_and_length_and_duplicates_and_duplicates(self):
        self.assertEqual(Repeat([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_list_with_order_and_length_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(Repeat([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_list_with_order_and_length_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(Repeat([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_list_with_order_and_length_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(Repeat([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_list_with_order_and_length_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(Repeat([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_list_with_order_and_length_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(Repeat([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_list_with_order_and_length_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(Repeat([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_list_with_order_and_length_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and