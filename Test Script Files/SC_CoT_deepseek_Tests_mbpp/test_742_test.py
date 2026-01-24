import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_tetrahedron(3), 12.99038105676658)

    def test_boundary_case(self):
        self.assertAlmostEqual(area_tetrahedron(0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(area_tetrahedron(1), 1.9999999999999998)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area_tetrahedron('a')
