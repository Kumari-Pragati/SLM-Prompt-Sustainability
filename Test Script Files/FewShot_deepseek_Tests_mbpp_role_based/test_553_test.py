import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(tuple_to_float((1, 2, 3)), 1.23)

    def test_edge_case(self):
        self.assertAlmostEqual(tuple_to_float((0, 0, 0)), 0.00)

    def test_boundary_case(self):
        self.assertAlmostEqual(tuple_to_float((9, 9)), 9.9)

    def test_single_digit(self):
        self.assertAlmostEqual(tuple_to_float((5)), 5.0)

    def test_large_number(self):
        self.assertAlmostEqual(tuple_to_float((1, 2, 3, 4, 5, 6, 7, 8, 9)), 1.23456789)

    def test_negative_number(self):
        self.assertAlmostEqual(tuple_to_float((-1, -2, -3)), -1.23)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_to_float(123)

        with self.assertRaises(TypeError):
            tuple_to_float("123")

        with self.assertRaises(TypeError):
            tuple_to_float((1, "2", 3))
