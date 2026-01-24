import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5]), [2, 4])

    def test_empty_list(self):
        self.assertEqual(remove_odd([]), [])

    def test_all_odd(self):
        self.assertEqual(remove_odd([1, 3, 5]), [])

    def test_all_even(self):
        self.assertEqual(remove_odd([2, 4, 6]), [2, 4, 6])

    def test_mixed_numbers(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_single_element(self):
        self.assertEqual(remove_odd([2]), [2])

    def test_single_odd_element(self):
        self.assertEqual(remove_odd([1]), [])

    def test_large_numbers(self):
        self.assertEqual(remove_odd(list(range(1, 101))), list(range(2, 101, 2)))
