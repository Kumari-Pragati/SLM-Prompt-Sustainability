import unittest
from mbpp_646_code import No_of_cubes

class TestNoOfCubes(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(No_of_cubes(3, 1), 1)
        self.assertEqual(No_of_cubes(6, 3), 27)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(No_of_cubes(0, 0), 0)
        self.assertEqual(No_of_cubes(1, 0), 1)
        self.assertEqual(No_of_cubes(1, 1), 1)
        self.assertEqual(No_of_cubes(2, 0), 8)
        self.assertEqual(No_of_cubes(2, 2), 8)

    def test_negative_input(self):
        self.assertRaises(ValueError, No_of_cubes, -1, 1)
        self.assertRaises(ValueError, No_of_cubes, 1, -1)

    def test_zero_input(self):
        self.assertRaises(ValueError, No_of_cubes, 0, 0)
        self.assertRaises(ValueError, No_of_cubes, 0, 1)
        self.assertRaises(ValueError, No_of_cubes, 1, 0)
