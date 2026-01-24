import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertAlmostEqual(area_tetrahedron(1), 1.7320508075688772)
        self.assertAlmostEqual(area_tetrahedron(2), 18.849556327596444)

    def test_edge_cases(self):
        self.assertAlmostEqual(area_tetrahedron(0), 0)
        self.assertAlmostEqual(area_tetrahedron(-1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            area_tetrahedron('a')
        with self.assertRaises(TypeError):
            area_tetrahedron(None)
