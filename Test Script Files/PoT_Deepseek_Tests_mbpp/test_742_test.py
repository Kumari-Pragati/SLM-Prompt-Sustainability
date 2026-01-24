import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_tetrahedron(2), 12.58840740696505)

    def test_edge_case(self):
        self.assertAlmostEqual(area_tetrahedron(0), 0)

    def test_boundary_case(self):
        self.assertAlmostEqual(area_tetrahedron(1), 4.330127018922194)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area_tetrahedron("2")

        with self.assertRaises(ValueError):
            area_tetrahedron(-2)
