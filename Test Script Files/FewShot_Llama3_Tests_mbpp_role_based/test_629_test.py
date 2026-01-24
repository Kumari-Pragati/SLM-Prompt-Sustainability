import unittest
from mbpp_629_code import Split

class TestSplit(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_single_even_number(self):
        self.assertEqual(Split([4]), [4])

    def test_single_odd_number(self):
        self.assertEqual(Split([5]), [])

    def test_multiple_even_numbers(self):
        self.assertEqual(Split([2, 4, 6]), [2, 4, 6])

    def test_multiple_odd_numbers(self):
        self.assertEqual(Split([1, 3, 5]), [])

    def test_mixed_list(self):
        self.assertEqual(Split([2, 4, 1, 3, 5, 6]), [2, 4, 6])

    def test_list_with_duplicates(self):
        self.assertEqual(Split([2, 4, 2, 6, 4, 6]), [2, 4, 6])
