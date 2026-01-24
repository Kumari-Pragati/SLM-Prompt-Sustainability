import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5]), [2, 4])

    def test_empty_list(self):
        self.assertEqual(remove_odd([]), [])

    def test_all_odd_numbers(self):
        self.assertEqual(remove_odd([1, 3, 5, 7, 9]), [])

    def test_all_even_numbers(self):
        self.assertEqual(remove_odd([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_single_number(self):
        self.assertEqual(remove_odd([2]), [2])

    def test_single_odd_number(self):
        self.assertEqual(remove_odd([1]), [])

    def test_single_even_number(self):
        self.assertEqual(remove_odd([2]), [2])

    def test_duplicate_numbers(self):
        self.assertEqual(remove_odd([1, 1, 2, 2, 3, 3]), [2, 2])

    def test_large_numbers(self):
        self.assertEqual(remove_odd([100, 200, 300, 400, 500]), [200, 400])
