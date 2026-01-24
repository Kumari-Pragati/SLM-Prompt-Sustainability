import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_remove_odd_with_even_numbers(self):
        self.assertEqual(remove_odd([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_remove_odd_with_mixed_numbers(self):
        self.assertEqual(remove_odd([2, 3, 4, 5, 6]), [2, 4, 6])

    def test_remove_odd_with_only_odd_numbers(self):
        self.assertEqual(remove_odd([1, 3, 5, 7]), [])

    def test_remove_odd_with_only_even_numbers(self):
        self.assertEqual(remove_odd([2, 4, 6]), [2, 4, 6])

    def test_remove_odd_with_empty_list(self):
        self.assertEqual(remove_odd([]), [])
