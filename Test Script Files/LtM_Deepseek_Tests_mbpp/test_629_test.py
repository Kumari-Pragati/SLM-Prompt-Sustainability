import unittest
from mbpp_629_code import Split

class TestSplit(unittest.TestCase):
    def test_simple_even_numbers(self):
        self.assertEqual(Split([1, 2, 3, 4]), [2, 4])

    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_all_odd_numbers(self):
        self.assertEqual(Split([1, 3, 5, 7]), [])

    def test_mixed_numbers(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_large_numbers(self):
        self.assertEqual(Split([1000000000, 2000000000, 3000000000]), [1000000000, 2000000000, 3000000000])

    def test_negative_even_numbers(self):
        self.assertEqual(Split([-2, -4, -6]), [-2, -4, -6])

    def test_negative_odd_numbers(self):
        self.assertEqual(Split([-1, -3, -5]), [])

    def test_mixed_negative_numbers(self):
        self.assertEqual(Split([-1, 2, -3, 4]), [2, 4])
