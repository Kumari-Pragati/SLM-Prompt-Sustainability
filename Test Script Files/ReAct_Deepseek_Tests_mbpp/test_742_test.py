import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_tetrahedron(3), 5.196152422706632)

    def test_zero_side(self):
        self.assertEqual(area_tetrahedron(0), 0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(-1)

    def test_large_number(self):
        self.assertAlmostEqual(area_tetrahedron(1000), 1732050.8075688772)
