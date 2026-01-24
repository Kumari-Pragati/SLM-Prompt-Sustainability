import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):

    def test_area_tetrahedron_positive(self):
        self.assertAlmostEqual(area_tetrahedron(5), 34.643416107254924)

    def test_area_tetrahedron_zero(self):
        with self.assertRaises(TypeError):
            area_tetrahedron(0)

    def test_area_tetrahedron_negative(self):
        with self.assertRaises(TypeError):
            area_tetrahedron(-5)

    def test_area_tetrahedron_non_numeric(self):
        with self.assertRaises(TypeError):
            area_tetrahedron('five')
