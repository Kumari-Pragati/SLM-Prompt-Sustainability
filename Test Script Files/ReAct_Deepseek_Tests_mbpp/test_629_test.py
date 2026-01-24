import unittest
from mbpp_629_code import Split

class TestSplitFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Split([1, 2, 3, 4, 5]), [2, 4])

    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_all_odd_numbers(self):
        self.assertEqual(Split([1, 3, 5, 7, 9]), [])

    def test_all_even_numbers(self):
        self.assertEqual(Split([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])

    def test_mixed_numbers(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_single_even_number(self):
        self.assertEqual(Split([2]), [2])

    def test_single_odd_number(self):
        self.assertEqual(Split([1]), [])

    def test_negative_numbers(self):
        self.assertEqual(Split([-2, -4, -6, -8, -10]), [-2, -4, -6, -8, -10])

    def test_zero(self):
        self.assertEqual(Split([0]), [0])
