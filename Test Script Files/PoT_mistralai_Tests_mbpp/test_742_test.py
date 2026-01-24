import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(area_tetrahedron(3), 16.9699)

    def test_edge_case_zero(self):
        self.assertAlmostEqual(area_tetrahedron(0), 0)

    def test_edge_case_one(self):
        self.assertAlmostEqual(area_tetrahedron(1), 3.4641)

    def test_edge_case_negative(self):
        self.assertAlmostEqual(area_tetrahedron(-1), 0)

    def test_boundary_case_small(self):
        self.assertAlmostEqual(area_tetrahedron(0.1), 0.3464)

    def test_boundary_case_large(self):
        self.assertAlmostEqual(area_tetrahedron(100), 34640)
