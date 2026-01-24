import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 2, 1], 5), 3)

    def test_edge_case_empty_array(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(get_Odd_Occurrence([1], 1), 1)

    def test_boundary_case_minimum_maximum_values(self):
        self.assertEqual(get_Odd_Occurrence([-1, -1, -1, 0, 0, 1, 1], 7), -1)

    def test_complex_case_multiple_odd_occurrences(self):
        self.assertEqual(get_Odd_Occurrence([1, 1, 2, 2, 3, 3, 4, 4, 9, 9, 5], 11), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_Odd_Occurrence("1, 2, 3, 2, 1", 5)
