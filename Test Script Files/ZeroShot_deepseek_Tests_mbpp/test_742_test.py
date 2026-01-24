import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):

    def test_positive_side(self):
        self.assertAlmostEqual(area_tetrahedron(3), 31.748537585120863)

    def test_zero_side(self):
        self.assertEqual(area_tetrahedron(0), 0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(-3)
