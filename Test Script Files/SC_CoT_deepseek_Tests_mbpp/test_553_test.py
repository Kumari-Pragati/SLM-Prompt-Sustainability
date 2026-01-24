import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(tuple_to_float((1, 2, 3)), 1.23)

    def test_single_digit(self):
        self.assertAlmostEqual(tuple_to_float((5)), 5.0)

    def test_zero(self):
        self.assertAlmostEqual(tuple_to_float((0, 0, 0)), 0.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(tuple_to_float((-1, -2, -3)), -1.23)

    def test_large_numbers(self):
        self.assertAlmostEqual(tuple_to_float((100, 200, 300)), 1.23)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(tuple_to_float(()), 0.0)

    def test_edge_case_one_element_tuple(self):
        self.assertAlmostEqual(tuple_to_float((1)), 1.0)

    def test_edge_case_two_elements_tuple(self):
        self.assertAlmostEqual(tuple_to_float((1, 2)), 1.2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_to_float(123)

        with self.assertRaises(TypeError):
            tuple_to_float('123')

        with self.assertRaises(TypeError):
            tuple_to_float((1, 2, '3'))
