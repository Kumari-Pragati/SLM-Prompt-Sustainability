import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(tuple_to_float((1, 2, 3)), 1.23)

    def test_zero_input(self):
        self.assertEqual(tuple_to_float((0,)), 0.0)

    def test_negative_input(self):
        self.assertEqual(tuple_to_float((-1, 2, 3)), -1.23)

    def test_multiple_zeros_input(self):
        self.assertEqual(tuple_to_float((0, 0, 0)), 0.0)

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            tuple_to_float(())

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            tuple_to_float(('a', 2, 3))

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            tuple_to_float('a')
