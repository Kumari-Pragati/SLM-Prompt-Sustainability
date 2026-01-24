import unittest
from mbpp_742_code import sqrt
from 742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):

    def test_area_tetrahedron_positive(self):
        for side in [1, 2, 3, 4, 5]:
            with self.subTest(f"side={side}"):
                result = area_tetrahedron(side)
                expected = sqrt(3) * side ** 2
                self.assertAlmostEqual(result, expected, delta=0.01)

    def test_area_tetrahedron_zero(self):
        result = area_tetrahedron(0)
        self.assertEqual(result, 0)

    def test_area_tetrahedron_negative(self):
        result = area_tetrahedron(-1)
        self.assertEqual(result, 0)
