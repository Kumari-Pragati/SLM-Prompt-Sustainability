import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(lateralsurface_cuboid(1,2,3), 12)
        self.assertEqual(lateralsurface_cuboid(4,5,6), 24)
        self.assertEqual(lateralsurface_cuboid(7,8,9), 36)

    def test_edge_cases(self):
        self.assertEqual(lateralsurface_cuboid(0,0,0), 0)
        self.assertEqual(lateralsurface_cuboid(1,1,0), 2)
        self.assertEqual(lateralsurface_cuboid(0,1,1), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsurface_cuboid('a',2,3)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(1,'b',3)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(1,2,'c')
