import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(round_and_sum([1.123, 2.345, 3.456]), 6)

    def test_edge_case_single_element(self):
        self.assertEqual(round_and_sum([1.1]), 1)

    def test_boundary_case_empty_list(self):
        self.assertEqual(round_and_sum([]), 0)

    def test_corner_case_all_same_number(self):
        self.assertEqual(round_and_sum([1.1, 1.1, 1.1]), 3)

    def test_corner_case_all_different_numbers(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 6)

    def test_corner_case_all_integers(self):
        self.assertEqual(round_and_sum([1, 2, 3]), 6)

    def test_corner_case_all_same_integer(self):
        self.assertEqual(round_and_sum([1, 1, 1]), 3)

    def test_corner_case_all_negative_numbers(self):
        self.assertEqual(round_and_sum([-1.1, -2.2, -3.3]), -6)

    def test_corner_case_all_negative_integers(self):
        self.assertEqual(round_and_sum([-1, -2, -3]), -6)

    def test_corner_case_all_negative_and_positive_numbers(self):
        self.assertEqual(round_and_sum([-1.1, 2.2, -3.3]), -0.1)
