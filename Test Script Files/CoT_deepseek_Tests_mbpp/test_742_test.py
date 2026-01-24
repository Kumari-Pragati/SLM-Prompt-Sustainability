import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):

    def test_positive_side(self):
        self.assertAlmostEqual(area_tetrahedron(3), 54.93061443340549)

    def test_zero_side(self):
        self.assertEqual(area_tetrahedron(0), 0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(-3)

    def test_non_numeric_side(self):
        with self.assertRaises(TypeError):
            area_tetrahedron('a')
