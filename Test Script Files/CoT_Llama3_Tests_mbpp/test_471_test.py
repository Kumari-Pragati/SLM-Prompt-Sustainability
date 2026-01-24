import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 4), 1)

    def test_edge_case_zero(self):
        self.assertEqual(find_remainder([1, 2, 3], 0, 4), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_remainder([1], 1, 4), 1)

    def test_edge_case_empty_array(self):
        self.assertEqual(find_remainder([], 0, 4), 1)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            find_remainder([1, 2, 3], 'a', 4)

    def test_invalid_input_non_positive_integer(self):
        with self.assertRaises(TypeError):
            find_remainder([1, 2, 3], 0, -4)

    def test_invalid_input_non_array(self):
        with self.assertRaises(TypeError):
            find_remainder('a', 3, 4)

    def test_invalid_input_non_integer_array(self):
        with self.assertRaises(TypeError):
            find_remainder([1.5, 2, 3], 3, 4)
