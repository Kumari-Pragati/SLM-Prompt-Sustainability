import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):

    def test_simple_positive(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 4*math.pi)

    def test_typical_positive(self):
        self.assertAlmostEqual(surfacearea_sphere(3.14), 12.566368349894953)

    def test_edge_zero(self):
        self.assertEqual(surfacearea_sphere(0), 0)

    def test_edge_negative(self):
        self.assertAlmostEqual(surfacearea_sphere(-1), 4*math.pi)

    def test_edge_large_positive(self):
        self.assertAlmostEqual(surfacearea_sphere(1e10), 4e20*math.pi)
