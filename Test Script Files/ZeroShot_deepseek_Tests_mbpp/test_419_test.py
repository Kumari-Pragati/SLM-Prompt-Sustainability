import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_round_and_sum_positive(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 6)

    def test_round_and_sum_negative(self):
        self.assertEqual(round_and_sum([-1.1, -2.2, -3.3]), -6)

    def test_round_and_sum_mixed(self):
        self.assertEqual(round_and_sum([1.1, -2.2, 3.3]), 2)

    def test_round_and_sum_zero(self):
        self.assertEqual(round_and_sum([0, 0, 0]), 0)

    def test_round_and_sum_single_element(self):
        self.assertEqual(round_and_sum([1]), 1)

    def test_round_and_sum_empty(self):
        self.assertEqual(round_and_sum([]), 0)
