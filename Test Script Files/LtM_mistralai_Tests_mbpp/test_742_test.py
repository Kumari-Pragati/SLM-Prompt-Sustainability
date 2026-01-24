import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):
    def test_simple_input(self):
        self.assertAlmostEqual(area_tetrahedron(1), 2.0)
        self.assertAlmostEqual(area_tetrahedron(2), 6.0)
        self.assertAlmostEqual(area_tetrahedron(3), 11.320701754800244)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(area_tetrahedron(0), 0)
        self.assertAlmostEqual(area_tetrahedron(1e-6), 0)
        self.assertAlmostEqual(area_tetrahedron(1e6), 196348253968637061.0)
