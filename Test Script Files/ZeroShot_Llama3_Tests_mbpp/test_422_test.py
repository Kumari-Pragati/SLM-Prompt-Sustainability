import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_find_Average_Of_Cube(self):
        self.assertEqual(find_Average_Of_Cube(1), 1.0)
        self.assertEqual(find_Average_Of_Cube(2), 8.0)
        self.assertEqual(find_Average_Of_Cube(3), 14.0)
        self.assertEqual(find_Average_Of_Cube(4), 24.0)
        self.assertEqual(find_Average_Of_Cube(5), 35.0)
        self.assertEqual(find_Average_Of_Cube(6), 48.0)
        self.assertEqual(find_Average_Of_Cube(7), 63.0)
        self.assertEqual(find_Average_Of_Cube(8), 80.0)
        self.assertEqual(find_Average_Of_Cube(9), 99.0)
        self.assertEqual(find_Average_Of_Cube(10), 121.0)

    def test_find_Average_Of_Cube_edge_cases(self):
        self.assertRaises(TypeError, find_Average_Of_Cube, 'a')
        self.assertRaises(TypeError, find_Average_Of_Cube, 0.5)
