import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(frequency([1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4], 4), 4)

    def test_negative_numbers(self):
        self.assertEqual(frequency([-1, -2, -3, -4, -2, -2, -3, -1, -4, -4, -4], -4), 3)

    def test_mixed_numbers(self):
        self.assertEqual(frequency([1, -2, 3, -4, 2, -2, 3, 1, -4, 4, -4], -4), 2)

    def test_zero(self):
        self.assertEqual(frequency([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0), 11)

    def test_empty_list(self):
        self.assertEqual(frequency([], 4), 0)

    def test_non_existing_number(self):
        self.assertEqual(frequency([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), 0)
