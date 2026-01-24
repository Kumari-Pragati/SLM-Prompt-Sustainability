import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(tuple_to_float((1.0, 2.0, 3.0)), 1.0, places=3)

    def test_edge_cases(self):
        self.assertAlmostEqual(tuple_to_float((0.0, 0.0, 0.0)), 0.0, places=3)
        self.assertAlmostEqual(tuple_to_float((1.1, 0.0, 0.0)), 1.1, places=3)
        self.assertAlmostEqual(tuple_to_float((0.0, 1.1, 0.0)), 1.1, places=3)
        self.assertAlmostEqual(tuple_to_float((0.0, 0.0, 1.1)), 1.1, places=3)

    def test_boundary_cases(self):
        self.assertAlmostEqual(tuple_to_float((-1.0, 0.0, 0.0)), -1.0, places=3)
        self.assertAlmostEqual(tuple_to_float((0.0, -1.0, 0.0)), -1.0, places=3)
        self.assertAlmostEqual(tuple_to_float((0.0, 0.0, -1.0)), -1.0, places=3)

    def test_invalid_input(self):
        self.assertRaises(ValueError, tuple_to_float, (1, 2, 3))
        self.assertRaises(ValueError, tuple_to_float, (1.0, 2, 3.0))
        self.assertRaises(ValueError, tuple_to_float, (1.0, 2.0, '3.0'))
