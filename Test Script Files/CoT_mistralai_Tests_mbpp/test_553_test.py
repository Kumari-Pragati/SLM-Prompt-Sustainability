import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(tuple_to_float((1.0, 2.0, 3.0)), 1.0, places=6)
        self.assertAlmostEqual(tuple_to_float((0.1, 0.2, 0.3)), 0.123, places=6)
        self.assertAlmostEqual(tuple_to_float((-1.0, -2.0, -3.0)), -1.0, places=6)

    def test_single_element(self):
        self.assertAlmostEqual(tuple_to_float((1.0)), 1.0, places=6)
        self.assertAlmostEqual(tuple_to_float((-1.0)), -1.0, places=6)

    def test_empty_tuple(self):
        self.assertIsInstance(tuple_to_float(()), TypeError)

    def test_non_numeric_input(self):
        self.assertIsInstance(tuple_to_float(('a', 'b', 'c')), TypeError)
        self.assertIsInstance(tuple_to_float((1, 'b', 3)), TypeError)
        self.assertIsInstance(tuple_to_float((1, 2, '3')), TypeError)
