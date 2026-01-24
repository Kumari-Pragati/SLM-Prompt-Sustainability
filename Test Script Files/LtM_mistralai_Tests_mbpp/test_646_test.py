import unittest
from mbpp_646_code import No_of_cubes

class TestNoOfCubes(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(No_of_cubes(1, 1), 1)
        self.assertEqual(No_of_cubes(2, 2), 8)
        self.assertEqual(No_of_cubes(3, 3), 27)

    def test_edge_input(self):
        self.assertEqual(No_of_cubes(0, 0), 0)
        self.assertEqual(No_of_cubes(1, 0), 1)
        self.assertEqual(No_of_cubes(2, 1), 2)
        self.assertEqual(No_of_cubes(3, 2), 9)

    def test_negative_input(self):
        self.assertRaises(ValueError, No_of_cubes, -1, 1)
        self.assertRaises(ValueError, No_of_cubes, 1, -1)

    def test_zero_input(self):
        self.assertRaises(ValueError, No_of_cubes, 0, 0)
