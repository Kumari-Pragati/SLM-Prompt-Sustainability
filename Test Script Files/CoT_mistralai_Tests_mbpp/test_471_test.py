import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 5), 3)
        self.assertEqual(find_remainder([4, 5, 6], 2, 3), 2)
        self.assertEqual(find_remainder([7, 8, 9], 3, 7), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_remainder([], 1, 2), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(find_remainder([1], 1, 2), 1)

    def test_edge_case_single_element_zero(self):
        self.assertEqual(find_remainder([0], 1, 2), 0)

    def test_edge_case_single_element_negative(self):
        self.assertEqual(find_remainder([-1], 1, 2), 1)

    def test_edge_case_list_of_zeros(self):
        self.assertEqual(find_remainder([0, 0, 0], 3, 3), 0)

    def test_edge_case_list_of_ones(self):
        self.assertEqual(find_remainder([1, 1, 1], 3, 3), 1)

    def test_edge_case_list_of_negatives(self):
        self.assertEqual(find_remainder([-1, -2, -3], 3, 3), 1)

    def test_edge_case_list_of_negatives_and_zeros(self):
        self.assertEqual(find_remainder([-1, 0, -2], 3, 3), 1)

    def test_invalid_input_list(self):
        self.assertRaises(TypeError, find_remainder, 'string', 1, 2)

    def test_invalid_input_lens(self):
        self.assertRaises(TypeError, find_remainder, [1, 2, 3], 'string', 2)

    def test_invalid_input_n(self):
        self.assertRaises(TypeError, find_remainder, [1, 2, 3], 1, 'string')
