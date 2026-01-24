import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(find_Volume(10, 20, 30), 3000)

    def test_zero_dimensions(self):
        self.assertEqual(find_Volume(0, 0, 0), 0)

    def test_negative_dimensions(self):
        with self.assertRaises(ValueError):
            find_Volume(-10, 20, 30)
        with self.assertRaises(ValueError):
            find_Volume(10, -20, 30)
        with self.assertRaises(ValueError):
            find_Volume(10, 20, -30)

    def test_non_numeric_dimensions(self):
        with self.assertRaises(TypeError):
            find_Volume('10', 20, 30)
        with self.assertRaises(TypeError):
            find_Volume(10, '20', 30)
        with self.assertRaises(TypeError):
            find_Volume(10, 20, '30')
