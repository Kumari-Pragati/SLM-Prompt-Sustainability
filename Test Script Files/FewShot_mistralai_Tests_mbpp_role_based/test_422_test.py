import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):
    def test_positive_integer(self):
        self.assertAlmostEqual(find_Average_Of_Cube(3), 2.166667, delta=0.000001)
        self.assertAlmostEqual(find_Average_Of_Cube(10), 106.066667, delta=0.000001)

    def test_zero(self):
        self.assertEqual(find_Average_Of_Cube(0), 0)

    def test_negative_integer(self):
        self.assertRaises(ValueError, find_Average_Of_Cube, -1)

    def test_floating_point(self):
        self.assertAlmostEqual(find_Average_Of_Cube(2.5), 13.377637, delta=0.000001)
