import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(round_and_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(round_and_sum([1.1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 10.6)

    def test_negative_numbers(self):
        self.assertEqual(round_and_sum([-1.1, -2.2, -3.3]), 10.6)

    def test_floats_and_integers(self):
        self.assertEqual(round_and_sum([1, 1.1, 2.2]), 7.2)
