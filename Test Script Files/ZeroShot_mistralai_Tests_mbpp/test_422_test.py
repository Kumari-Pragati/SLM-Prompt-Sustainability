import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_find_average_of_cube_with_positive_integer(self):
        self.assertAlmostEqual(find_Average_Of_Cube(3), 2.166667, delta=0.000001)
        self.assertAlmostEqual(find_Average_Of_Cube(4), 3.090909, delta=0.000001)
        self.assertAlmostEqual(find_Average_Of_Cube(5), 4.038462, delta=0.000001)

    def test_find_average_of_cube_with_zero(self):
        self.assertEqual(find_Average_Of_Cube(0), 0.0)

    def test_find_average_of_cube_with_negative_integer(self):
        self.assertRaises(ValueError, find_Average_Of_Cube, -1)
