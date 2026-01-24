import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(tuple_to_float((1.1, 2.2, 3.3)), 1.1 + 2.2 + 3.3)
        self.assertAlmostEqual(tuple_to_float((0.0, 0.0, 0.0)), 0.0)
        self.assertAlmostEqual(tuple_to_float((-1.1, -2.2, -3.3)), -1.1 - 2.2 - 3.3)

    def test_empty_input(self):
        self.assertRaises(ValueError, tuple_to_float, ())

    def test_single_input(self):
        self.assertRaises(ValueError, tuple_to_float, (1.1,))

    def test_non_float_input(self):
        self.assertRaises(TypeError, tuple_to_float, (1, 2, 3))
