import unittest
from mbpp_252_code import convert

class TestConvertFunction(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(convert([1, 2, 3]), [(1, 0), (2, 0), (3, 0)])

    def test_edge_case(self):
        self.assertEqual(convert([1, 2, 0]), [(1, 0), (2, 0), (0, 0)])

    def test_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3]), [(-1, 0), (-2, 0), (-3, 0)])

    def test_complex_numbers(self):
        self.assertEqual(convert([1+2j, 2-3j, 3+4j]), [(1+2j, 0), (2-3j, 0), (3+4j, 0)])

    def test_empty_list(self):
        self.assertEqual(convert([]), [])

    def test_single_element_list(self):
        self.assertEqual(convert([1]), [(1, 0)])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            convert("not a list")

    def test_invalid_input_structure(self):
        with self.assertRaises(TypeError):
            convert({1, 2, 3})
