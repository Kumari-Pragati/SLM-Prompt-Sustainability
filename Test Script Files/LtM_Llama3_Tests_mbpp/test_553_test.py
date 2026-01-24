import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(tuple_to_float((1, 2)), 1.2)

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            tuple_to_float(())

    def test_single_element_input(self):
        self.assertEqual(tuple_to_float((1,)), 1.0)

    def test_max_float_value(self):
        self.assertEqual(tuple_to_float((1.0e308,)), 1.0e308)

    def test_min_float_value(self):
        self.assertEqual(tuple_to_float((-1.0e308,)), -1.0e308)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            tuple_to_float("hello")

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            tuple_to_float((1, 2, 3, 4, 5))
