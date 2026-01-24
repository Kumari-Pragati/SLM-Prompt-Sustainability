import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(round_and_sum([1.5, 2.5, 3.5]), 12.0)

    def test_edge_case_zero(self):
        self.assertEqual(round_and_sum([0, 0, 0]), 0)

    def test_edge_case_one(self):
        self.assertEqual(round_and_sum([1.0]), 1.0)

    def test_edge_case_negative(self):
        self.assertEqual(round_and_sum([-1.5, -2.5, -3.5]), -12.0)

    def test_edge_case_empty(self):
        self.assertEqual(round_and_sum([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(round_and_sum([4.5]), 4.5)

    def test_edge_case_multiple_elements(self):
        self.assertEqual(round_and_sum([1.5, 2.5, 3.5, 4.5, 5.5]), 21.0)

    def test_edge_case_rounding(self):
        self.assertAlmostEqual(round_and_sum([1.499, 2.500, 3.501]), 8.0)
