import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(tuple_to_float((1, 2, 3)), 1.23)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(tuple_to_float((0, 0)), 0.0)
        self.assertAlmostEqual(tuple_to_float((9, 9)), 9.9)
        self.assertAlmostEqual(tuple_to_float((1, 9)), 1.9)
        self.assertAlmostEqual(tuple_to_float((9, 1)), 9.1)

    def test_edge_cases(self):
        self.assertAlmostEqual(tuple_to_float(()), 0.0)
        self.assertAlmostEqual(tuple_to_float((0)), 0.0)
        self.assertAlmostEqual(tuple_to_float((1, 0, 0)), 1.0)
        self.assertAlmostEqual(tuple_to_float((0, 1, 0)), 0.1)
        self.assertAlmostEqual(tuple_to_float((0, 0, 1)), 0.01)
        self.assertAlmostEqual(tuple_to_float((1, 2, 3, 4, 5)), 1.2345)
