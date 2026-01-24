import unittest
from mbpp_646_code import No_of_cubes

class TestNo_of_cubes(unittest.TestCase):

    def test_no_of_cubes(self):
        self.assertEqual(No_of_cubes(5, 2), 1)
        self.assertEqual(No_of_cubes(10, 3), 1)
        self.assertEqual(No_of_cubes(15, 4), 0)
        self.assertEqual(No_of_cubes(20, 5), 0)
        self.assertEqual(No_of_cubes(25, 6), 0)
        self.assertEqual(No_of_cubes(30, 7), 0)
        self.assertEqual(No_of_cubes(35, 8), 0)
        self.assertEqual(No_of_cubes(40, 9), 0)
        self.assertEqual(No_of_cubes(45, 10), 0)
        self.assertEqual(No_of_cubes(50, 11), 0)
        self.assertEqual(No_of_cubes(55, 12), 0)
        self.assertEqual(No_of_cubes(60, 13), 0)
        self.assertEqual(No_of_cubes(65, 14), 0)
        self.assertEqual(No_of_cubes(70, 15), 0)
        self.assertEqual(No_of_cubes(75, 16), 0)
        self.assertEqual(No_of_cubes(80, 17), 0)
        self.assertEqual(No_of_cubes(85, 18), 0)
        self.assertEqual(No_of_cubes(90, 19), 0)
        self.assertEqual(No_of_cubes(95, 20), 0)
        self.assertEqual(No_of_cubes(100, 21), 0)
