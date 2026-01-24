import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(is_polite(10), 11.0, delta=0.01)
        self.assertAlmostEqual(is_polite(100), 101.0, delta=0.01)
        self.assertAlmostEqual(is_polite(1000), 1001.0, delta=0.01)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(is_polite(0), 1.0, delta=0.01)
        self.assertAlmostEqual(is_polite(1), 2.0, delta=0.01)
        self.assertAlmostEqual(is_polite(2), 3.0, delta=0.01)
        self.assertAlmostEqual(is_polite(math.e), math.e + 1.0, delta=0.01)
        self.assertAlmostEqual(is_polite(math.pi), math.pi + 1.0, delta=0.01)

    def test_invalid_input(self):
        self.assertRaises(TypeError, is_polite, 'string')
        self.assertRaises(TypeError, is_polite, -1)
        self.assertRaises(TypeError, is_polite, float('inf'))
        self.assertRaises(TypeError, is_polite, float('-inf'))
        self.assertRaises(TypeError, is_polite, complex(1, 2))
