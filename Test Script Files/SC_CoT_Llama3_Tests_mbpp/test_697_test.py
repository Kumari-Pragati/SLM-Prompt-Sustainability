import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_even([1, 2, 3, 4, 5, 6]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_even([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_even([10]), 1)

    def test_edge_case_single_non_even_element(self):
        self.assertEqual(count_even([7]), 0)

    def test_edge_case_single_even_element(self):
        self.assertEqual(count_even([4]), 1)

    def test_edge_case_multiple_even_elements(self):
        self.assertEqual(count_even([2, 4, 6, 8]), 4)

    def test_edge_case_multiple_non_even_elements(self):
        self.assertEqual(count_even([1, 3, 5, 7, 9]), 0)

    def test_edge_case_mixed_elements(self):
        self.assertEqual(count_even([1, 2, 3, 4, 5, 6, 7, 8, 9]), 4)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            count_even("hello")

    def test_invalid_input_empty_string(self):
        with self.assertRaises(TypeError):
            count_even("")
