import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 4), 1)

    def test_edge_case_zero_length_array(self):
        self.assertEqual(find_remainder([], 0, 4), 0)

    def test_edge_case_zero_remainder(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 0), 0)

    def test_edge_case_negative_remainder(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, -4), 1)

    def test_edge_case_large_remainder(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 1000), 1)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_remainder("abc", 3, 4)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            find_remainder([1, 2, "three"], 3, 4)
