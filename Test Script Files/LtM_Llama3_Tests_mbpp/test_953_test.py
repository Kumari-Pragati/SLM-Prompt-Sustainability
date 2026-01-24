import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(subset([], 0), 0)

    def test_single_element_input(self):
        self.assertEqual(subset([1], 1), 1)

    def test_multiple_elements_input(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 3], 6), 3)

    def test_edge_case_input(self):
        self.assertEqual(subset([1, 1, 1, 1, 1, 1], 6), 6)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            subset("abc", 5)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            subset([1, 2, 3], "five")
