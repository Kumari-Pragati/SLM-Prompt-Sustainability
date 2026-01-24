import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(round_and_sum([1.5, 2.5, 3.5]), 12.0)

    def test_edge_case_empty_list(self):
        self.assertEqual(round_and_sum([]), 0.0)

    def test_edge_case_single_element(self):
        self.assertEqual(round_and_sum([4.5]), 4.5)

    def test_edge_case_zero_length_list(self):
        self.assertEqual(round_and_sum([0.0]), 0.0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(round_and_sum([-1.5, -2.5, -3.5]), -12.0)

    def test_edge_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            round_and_sum(['a', 'b', 'c'])

    def test_edge_case_mixed_type_input(self):
        with self.assertRaises(TypeError):
            round_and_sum([1, 'a', 2.5])

    def test_edge_case_list_of_strings(self):
        with self.assertRaises(TypeError):
            round_and_sum(['a', 'b', 'c'])

    def test_edge_case_list_of_mixed_types(self):
        with self.assertRaises(TypeError):
            round_and_sum([1, 'a', 2.5, 'c'])
