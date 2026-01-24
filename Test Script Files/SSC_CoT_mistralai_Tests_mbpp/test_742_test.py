import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):
    def test_normal_input(self):
        self.assertAlmostEqual(area_tetrahedron(3), 8.660254037844476)

    def test_edge_input(self):
        self.assertAlmostEqual(area_tetrahedron(0), 0)
        self.assertAlmostEqual(area_tetrahedron(1), 2.8284271247461903)
        self.assertAlmostEqual(area_tetrahedron(1000), 999999.9999999998)

    def test_negative_input(self):
        self.assertRaises(ValueError, area_tetrahedron, -1)

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, area_tetrahedron, 'string')
