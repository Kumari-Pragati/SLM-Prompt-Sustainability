import unittest
from mbpp_629_code import Split

class TestSplit(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_odd_numbers(self):
        self.assertEqual(Split([1, 3, 5, 7, 9]), [])

    def test_mixed_numbers(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6, 7, 8, 9]), [2, 4, 6, 8])

    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_negative_numbers(self):
        self.assertEqual(Split([-1, -2, -3, -4, -5, -6]), [-2, -4, -6])

    def test_zero(self):
        self.assertEqual(Split([0]), [0])
