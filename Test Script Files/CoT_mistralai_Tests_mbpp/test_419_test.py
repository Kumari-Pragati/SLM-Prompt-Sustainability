import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(round_and_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(round_and_sum([3.14]), 3)

    def test_positive_numbers(self):
        self.assertEqual(round_and_sum([1.23, 4.56, 7.89]), 31)

    def test_negative_numbers(self):
        self.assertEqual(round_and_sum([-1.23, -4.56, -7.89]), 31)

    def test_mixed_numbers(self):
        self.assertEqual(round_and_sum([1.23, -4.56, 7.89, -0.12]), 14)

    def test_zero(self):
        self.assertEqual(round_and_sum([0.0]), 0)

    def test_large_numbers(self):
        self.assertEqual(round_and_sum([1e10, 2e10, 3e10]), 6e11)

    def test_small_numbers(self):
        self.assertEqual(round_and_sum([1e-10, 2e-10, 3e-10]), 6e-10)

    def test_floats_and_integers(self):
        self.assertEqual(round_and_sum([1, 2.5, 3]), 15)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            round_and_sum([1, "two", 3])
