import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(lateralsurface_cube(3), 36)

    def test_boundary_condition(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            lateralsurface_cube(-1)
