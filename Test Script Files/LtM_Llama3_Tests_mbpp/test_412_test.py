import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_odd([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_odd([1]), [])

    def test_even_list(self):
        self.assertEqual(remove_odd([2, 4, 6]), [2, 4, 6])

    def test_odd_list(self):
        self.assertEqual(remove_odd([1, 3, 5]), [])

    def test_mixed_list(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5]), [2, 4])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_odd([1, 2, 2, 3, 4, 4, 5]), [2, 2, 4, 4])

    def test_list_with_duplicates_and_odd(self):
        self.assertEqual(remove_odd([1, 2, 2, 3, 4, 4, 5, 7]), [2, 2, 4, 4])
