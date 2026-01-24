import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(area_tetrahedron(1), math.sqrt(3), delta=0.01)
        self.assertAlmostEqual(area_tetrahedron(2), 6 * math.sqrt(3))
        self.assertAlmostEqual(area_tetrahedron(3), 9 * math.sqrt(3))

    def test_zero(self):
        self.assertAlmostEqual(area_tetrahedron(0), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(area_tetrahedron(-1), 0)
        self.assertAlmostEqual(area_tetrahedron(-2), 0)
        self.assertAlmostEqual(area_tetrahedron(-3), 0)
