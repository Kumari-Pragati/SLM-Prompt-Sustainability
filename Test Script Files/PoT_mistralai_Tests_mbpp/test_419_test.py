import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 30)

    def test_edge_case_zero_length(self):
        self.assertEqual(round_and_sum([]), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(round_and_sum([-1.1, -2.2, -3.3]), -30)

    def test_edge_case_floats_with_same_value(self):
        self.assertEqual(round_and_sum([1.1, 1.1, 1.1]), 4)

    def test_edge_case_floats_with_different_values(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 30)

    def test_corner_case_zero_and_negative_numbers(self):
        self.assertEqual(round_and_sum([0, -1.1, -2.2, -3.3]), -6)
