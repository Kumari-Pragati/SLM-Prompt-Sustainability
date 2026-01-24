import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 6)

    def test_boundary_conditions(self):
        self.assertEqual(round_and_sum([0]), 0)
        self.assertEqual(round_and_sum([1]), 1)
        self.assertEqual(round_and_sum([-1]), -1)
        self.assertEqual(round_and_sum([1.0]), 1)
        self.assertEqual(round_and_sum([-1.0]), -1)

    def test_edge_cases(self):
        self.assertEqual(round_and_sum([]), 0)
        self.assertEqual(round_and_sum([1.5]), 1)
        self.assertEqual(round_and_sum([1.4999999999999998]), 1)
        self.assertEqual(round_and_sum([-1.5]), -1)
        self.assertEqual(round_and_sum([-1.4999999999999998]), -1)

    def test_complex_cases(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3, -1.1, -2.2, -3.3]), 0)
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3, -1.1, -2.2, -3.3, 0]), 0)
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3, -1.1, -2.2, -3.3, 0.5]), 0.5)
