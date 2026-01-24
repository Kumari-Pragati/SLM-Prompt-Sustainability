import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Repeat([]), [])

    def test_single_element_list(self):
        self.assertEqual(Repeat([1]), [])

    def test_no_duplicates(self):
        self.assertEqual(Repeat([1, 2, 3]), [])

    def test_duplicates(self):
        self.assertEqual(Repeat([1, 1, 2, 2, 3]), [1, 2])

    def test_duplicates_in_order(self):
        self.assertEqual(Repeat([1, 2, 2, 3, 3, 3]), [1, 2, 3])

    def test_duplicates_out_of_order(self):
        self.assertEqual(Repeat([3, 2, 1, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_with_duplicates(self):
        self.assertEqual(Repeat([1, 1, 2, 2, 2, 3, 3, 3]), [1, 2, 3])

    def test_duplicates_with_duplicates_out_of_order(self):
        self.assertEqual(Repeat([3, 2, 2, 1, 1, 1, 3, 3, 3]), [1, 2, 3])
