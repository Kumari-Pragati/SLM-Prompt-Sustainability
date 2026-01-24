import unittest
from mbpp_554_code import Split

class TestSplit(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Split([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_all_even_numbers(self):
        self.assertEqual(Split([2, 4, 6, 8]), [])

    def test_all_odd_numbers(self):
        self.assertEqual(Split([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_mixed_numbers(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_negative_numbers(self):
        self.assertEqual(Split([-1, -2, -3, -4, -5]), [-1, -3, -5])

    def test_zero(self):
        self.assertEqual(Split([0]), [])
