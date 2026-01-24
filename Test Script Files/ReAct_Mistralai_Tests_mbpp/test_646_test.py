import unittest
from mbpp_646_code import No_of_cubes

class TestNoOfCubes(unittest.TestCase):

    def test_positive_integer_arguments(self):
        self.assertEqual(No_of_cubes(3, 1), 27)
        self.assertEqual(No_of_cubes(4, 2), 64)
        self.assertEqual(No_of_cubes(5, 3), 125)

    def test_zero_arguments(self):
        self.assertEqual(No_of_cubes(0, 0), 0)
        self.assertEqual(No_of_cubes(0, 1), 0)

    def test_negative_integer_arguments(self):
        self.assertRaises(ValueError, No_of_cubes, -1, 1)
        self.assertRaises(ValueError, No_of_cubes, 1, -1)

    def test_floating_point_arguments(self):
        self.assertRaises(TypeError, No_of_cubes, 3.5, 1)
        self.assertRaises(TypeError, No_of_cubes, 1, 3.5)

    def test_non_integer_arguments(self):
        self.assertRaises(TypeError, No_of_cubes, 'a', 1)
        self.assertRaises(TypeError, No_of_cubes, 1, 'a')
