import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(area_tetrahedron(1), math.sqrt(3), places=5)

    def test_boundary_condition(self):
        self.assertAlmostEqual(area_tetrahedron(0), 0, places=5)

    def test_edge_condition(self):
        self.assertAlmostEqual(area_tetrahedron(1000), 1000*math.sqrt(3), places=5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area_tetrahedron("invalid")
