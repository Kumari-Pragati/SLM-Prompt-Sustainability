import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):

    def test_find_volume(self):
        self.assertEqual(find_Volume(1,2,3), 3.0)
        self.assertEqual(find_Volume(4,5,6), 12.0)
        self.assertEqual(find_Volume(7,8,9), 168.0)
        self.assertEqual(find_Volume(10,20,30), 6000.0)
        self.assertEqual(find_Volume(0,0,0), 0.0)

    def test_find_volume_zero(self):
        self.assertEqual(find_Volume(0,0,0), 0.0)
        self.assertEqual(find_Volume(0,0,1), 0.0)
        self.assertEqual(find_Volume(0,1,0), 0.0)
        self.assertEqual(find_Volume(0,1,1), 0.0)

    def test_find_volume_negative(self):
        with self.assertRaises(TypeError):
            find_Volume(-1,2,3)
        with self.assertRaises(TypeError):
            find_Volume(1,-2,3)
        with self.assertRaises(TypeError):
            find_Volume(1,2,-3)
