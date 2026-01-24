import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 11)

    def test_edge_case_single_element(self):
        self.assertEqual(round_and_sum([1.1]), 1)

    def test_boundary_case_zero(self):
        self.assertEqual(round_and_sum([0, 0]), 0)

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(round_and_sum([-1.1, -2.2]), -3)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            round_and_sum(123)

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            round_and_sum(['a', 'b', 'c'])
