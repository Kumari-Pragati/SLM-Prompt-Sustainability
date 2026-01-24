import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):

    def test_positive_side(self):
        self.assertAlmostEqual(area_tetrahedron(1), math.sqrt(3))
        self.assertAlmostEqual(area_tetrahedron(2), 4 * math.sqrt(3))
        self.assertAlmostEqual(area_tetrahedron(3), 9 * math.sqrt(3))

    def test_zero_side(self):
        self.assertEqual(area_tetrahedron(0), 0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(-1)

    def test_large_number(self):
        self.assertAlmostEqual(area_tetrahedron(10000), 10000**2 * math.sqrt(3))
