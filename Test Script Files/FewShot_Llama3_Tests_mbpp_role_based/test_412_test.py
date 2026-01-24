import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_odd([]), [])

    def test_all_even(self):
        self.assertEqual(remove_odd([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_mixed_list(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_single_odd(self):
        self.assertEqual(remove_odd([1, 2, 3, 4]), [2, 4])

    def test_single_even(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 6]), [2, 4, 6])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_odd([1, 2, 2, 3, 4, 4, 5, 6, 6]), [2, 2, 4, 4, 6, 6])
