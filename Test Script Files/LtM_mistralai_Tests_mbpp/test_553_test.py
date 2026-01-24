import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):

    def test_simple(self):
        self.assertAlmostEqual(tuple_to_float((1.0, 2.0, 3.0)), 1.023)
        self.assertAlmostEqual(tuple_to_float((0.0, 0.0, 0.0)), 0.0)
        self.assertAlmostEqual(tuple_to_float((-1.0, -2.0, -3.0)), -1.023)

    def test_edge_and_boundary(self):
        self.assertAlmostEqual(tuple_to_float((float('inf'), 0.0, float('-inf'))), float('inf') - 0.0 + float('-inf'))
        self.assertAlmostEqual(tuple_to_float((float('nan'), float('nan'), float('nan'))), float('nan'))
        self.assertRaises(ValueError, tuple_to_float, (1, 2, '3'))

    def test_complex(self):
        self.assertAlmostEqual(tuple_to_float((float('-0'), float('0'), float('0'))), 0.0)
        self.assertAlmostEqual(tuple_to_float((float('-0'), float('0'), float('-0'))), -0.0)
        self.assertAlmostEqual(tuple_to_float((float('-0'), float('0'), float('-0.000001'))), -0.000001)
