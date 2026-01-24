import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 12)

    def test_negative_numbers(self):
        self.assertEqual(round_and_sum([-1.1, -2.2, -3.3]), 12)

    def test_zero(self):
        self.assertEqual(round_and_sum([0.0, 0.0, 0.0]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(round_and_sum([1.1, 0.0, -2.2]), 3)

    def test_empty_list(self):
        self.assertEqual(round_and_sum([]), 0)

    def test_list_with_one_element(self):
        self.assertEqual(round_and_sum([1.1]), 1)

    def test_list_with_floats_and_integers(self):
        self.assertEqual(round_and_sum([1.1, 2, -3.3]), 6)
