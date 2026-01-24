import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(tuple_to_float((1.2, 3.4)), 1.23)

    def test_edge_case_zero(self):
        self.assertAlmostEqual(tuple_to_float((0,)), 0.0)

    def test_edge_case_negative(self):
        self.assertAlmostEqual(tuple_to_float((-1.2,)), -1.2)

    def test_edge_case_empty(self):
        with self.assertRaises(ValueError):
            tuple_to_float(())

    def test_edge_case_single_element(self):
        self.assertAlmostEqual(tuple_to_float((1.2,)), 1.2)

    def test_edge_case_multiple_elements(self):
        self.assertAlmostEqual(tuple_to_float((1.2, 3.4, 5.6)), 1.23456)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            tuple_to_float("not a tuple")
