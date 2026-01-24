import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(tuple_int_str([(1, 2), (3, 4)]), ((1, 2), (3, 4)))

    def test_empty_input(self):
        self.assertEqual(tuple_int_str([]), ())

    def test_single_element_input(self):
        self.assertEqual(tuple_int_str([(1, 2)]), ((1, 2),))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            tuple_int_str("invalid input")

    def test_invalid_input_structure(self):
        with self.assertRaises(ValueError):
            tuple_int_str([(1, 2, 3)])

    def test_max_value_input(self):
        self.assertEqual(tuple_int_str([(2147483647, 2147483647), (2147483647, 2147483647)]), ((2147483647, 2147483647), (2147483647, 2147483647)))

    def test_min_value_input(self):
        self.assertEqual(tuple_int_str([(-2147483648, -2147483648), (-2147483648, -2147483648)]), ((-2147483648, -2147483648), (-2147483648, -2147483648)))
