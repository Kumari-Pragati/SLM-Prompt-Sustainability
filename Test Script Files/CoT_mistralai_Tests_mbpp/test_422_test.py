import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):
    def test_positive_integer(self):
        self.assertAlmostEqual(find_Average_Of_Cube(3), 2.1666667, delta=0.000001)
        self.assertAlmostEqual(find_Average_Of_Cube(10), 100.0, delta=0.000001)
        self.assertAlmostEqual(find_Average_Of_Cube(100), 1234567.0, delta=0.000001)

    def test_zero(self):
        self.assertEqual(find_Average_Of_Cube(0), 0.0)

    def test_negative_integer(self):
        self.assertEqual(find_Average_Of_Cube(-1), -1.0)
        self.assertEqual(find_Average_Of_Cube(-10), -1000.0)
        self.assertEqual(find_Average_Of_Cube(-100), -1234567.0)

    def test_non_integer(self):
        self.assertRaises(TypeError, find_Average_Of_Cube, 'not_an_integer')
        self.assertRaises(TypeError, find_Average_Of_Cube, 3.14)
