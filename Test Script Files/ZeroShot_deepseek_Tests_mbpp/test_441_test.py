import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceArea(unittest.TestCase):

    def test_surfacearea_cube(self):
        self.assertEqual(surfacearea_cube(1), 6)
        self.assertEqual(surfacearea_cube(2), 24)
        self.assertEqual(surfacearea_cube(0), 0)
        self.assertEqual(surfacearea_cube(-1), 6)
        self.assertNotEqual(surfacearea_cube(2), 25)
