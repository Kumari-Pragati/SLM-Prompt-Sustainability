import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lateralsurface_cube(3), 36)

    def test_zero_length(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            lateralsurface_cube(-1)

    def test_large_number(self):
        self.assertEqual(lateralsurface_cube(1000), 4000000)
