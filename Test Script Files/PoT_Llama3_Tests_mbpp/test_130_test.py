import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), (3, 3))

    def test_edge_case_empty_list(self):
        self.assertEqual(max_occurrences([]), (None, 0))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_edge_case_all_equal_elements(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), (1, 5))

    def test_edge_case_all_distinct_elements(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), (5, 1))

    def test_edge_case_max_occurrence_multiple(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), (5, 3))

    def test_edge_case_max_occurrence_single(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1, 1]), (1, 6))

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_occurrences("abc")

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            max_occurrences([1, "a", 2, 3])
