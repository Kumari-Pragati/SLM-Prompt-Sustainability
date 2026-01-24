import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tuple_to_float((1.0, 2.0, 3.0)), 1.023)

    def test_edge_case_zero(self):
        self.assertEqual(tuple_to_float((0.0, 0.0, 0.0)), 0.0)

    def test_edge_case_negative(self):
        self.assertEqual(tuple_to_float((-1.0, -2.0, -3.0)), -1.023)

    def test_boundary_case_single_element(self):
        self.assertEqual(tuple_to_float((1.0,)), 1.0)

    def test_boundary_case_empty_tuple(self):
        self.assertEqual(tuple_to_float(()), 0.0)

    def test_corner_case_mixed_types(self):
        self.assertRaises(TypeError, tuple_to_float, (1.0, 'str', 3.0))
