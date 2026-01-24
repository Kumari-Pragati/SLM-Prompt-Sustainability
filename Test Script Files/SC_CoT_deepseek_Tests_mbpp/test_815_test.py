import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDnf(unittest.TestCase):

    def test_typical_case(self):
        arr = [2, 0, 1, 2, 1, 0, 1, 2, 0, 1]
        expected_output = [0, 0, 1, 1, 1, 2, 2, 2, 0, 1]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_edge_case_single_element(self):
        arr = [0]
        expected_output = [0]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_edge_case_all_zeros(self):
        arr = [0, 0, 0, 0, 0]
        expected_output = [0, 0, 0, 0, 0]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_edge_case_all_ones(self):
        arr = [1, 1, 1, 1, 1]
        expected_output = [1, 1, 1, 1, 1]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_edge_case_all_twos(self):
        arr = [2, 2, 2, 2, 2]
        expected_output = [2, 2, 2, 2, 2]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_corner_case_mixed_elements(self):
        arr = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        expected_output = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_invalid_input_negative_numbers(self):
        arr = [-1, 0, 1, 2]
        with self.assertRaises(ValueError):
            sort_by_dnf(arr, len(arr))

    def test_invalid_input_non_integer_elements(self):
        arr = [0, 1, 2, 'a', 1, 2, 0, 1, 2]
        with self.assertRaises(TypeError):
            sort_by_dnf(arr, len(arr))
