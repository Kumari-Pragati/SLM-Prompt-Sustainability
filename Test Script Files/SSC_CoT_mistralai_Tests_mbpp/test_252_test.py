import unittest
from mbpp_252_code import pi, nan
from 252_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(convert(5), (5j, pi/2))
        self.assertAlmostEqual(convert(-5), (-5j, pi/2))
        self.assertAlmostEqual(convert(3+4j), (5, pi/4))
        self.assertAlmostEqual(convert(-3-4j), (-5, pi/4))

    def test_edge_and_boundary_cases(self):
        self.assertAlmostEqual(convert(0), (0j, 0))
        self.assertAlmostEqual(convert(1e-308), (1e-308j, pi))
        self.assertAlmostEqual(convert(-1e308), (-1e308j, pi))
        self.assertAlmostEqual(convert(1), (1, 0))
        self.assertAlmostEqual(convert(-1), (-1, 0))
        self.assertAlmostEqual(convert(pi), (1, pi/2))
        self.assertAlmostEqual(convert(-pi), (-1, pi/2))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, convert, 1.23)
        self.assertAlmostEqual(convert(nan), (nan, nan))
