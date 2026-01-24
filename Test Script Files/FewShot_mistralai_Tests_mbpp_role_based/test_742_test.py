import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):
    def test_positive_side(self):
        self.assertAlmostEqual(area_tetrahedron(3), 16.653333333333334)

    def test_zero_side(self):
        self.assertEqual(area_tetrahedron(0), 0)

    def test_negative_side(self):
        self.assertRaises(ValueError, area_tetrahedron, -1)

    def test_non_numeric_side(self):
        self.assertRaises(TypeError, area_tetrahedron, 'invalid')
