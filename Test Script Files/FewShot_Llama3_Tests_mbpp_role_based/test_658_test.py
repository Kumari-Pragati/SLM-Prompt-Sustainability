import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)

    def test_edge_case_empty_list(self):
        self.assertRaises(IndexError, max_occurrences, [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_edge_case_all_elements_equal(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), 1)

    def test_edge_case_all_elements_distinct(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_occurrences("Invalid input")
