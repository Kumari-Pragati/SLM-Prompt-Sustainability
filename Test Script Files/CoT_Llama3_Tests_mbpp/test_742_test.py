import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):

    def test_typical_input(self):
        self.assertAlmostEqual(area_tetrahedron(5), 12.49056605079443)

    def test_zero_input(self):
        with self.assertRaises(ZeroDivisionError):
            area_tetrahedron(0)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            area_tetrahedron(-5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            area_tetrahedron('five')

    def test_edge_case(self):
        self.assertAlmostEqual(area_tetrahedron(0.1), 0.030000000000000027)
