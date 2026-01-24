import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):

    def test_positive_integer(self):
        self.assertAlmostEqual(area_tetrahedron(3), 16.96991318367347, delta=0.01)

    def test_zero(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(-1)

    def test_non_number(self):
        with self.assertRaises(TypeError):
            area_tetrahedron('string')

    def test_float(self):
        self.assertAlmostEqual(area_tetrahedron(2.5), 12.2499578125, delta=0.01)

    def test_large_number(self):
        self.assertAlmostEqual(area_tetrahedron(100), 31622.77660168379, delta=0.01)
