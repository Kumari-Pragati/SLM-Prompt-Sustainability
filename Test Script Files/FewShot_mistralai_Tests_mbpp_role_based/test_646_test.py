import unittest
from mbpp_646_code import No_of_cubes

class TestNoOfCubes(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(No_of_cubes(3, 1), 27)
        self.assertEqual(No_of_cubes(4, 2), 64)
        self.assertEqual(No_of_cubes(5, 3), 125)

    def test_zero(self):
        self.assertEqual(No_of_cubes(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(No_of_cubes(-1, 0), 1)
        self.assertEqual(No_of_cubes(-2, 1), 8)
        self.assertEqual(No_of_cubes(-3, 2), 27)

    def test_negative_K(self):
        self.assertEqual(No_of_cubes(3, -1), 27)
        self.assertEqual(No_of_cubes(4, -2), 64)
        self.assertEqual(No_of_cubes(5, -3), 125)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, No_of_cubes, -1, -1)
        self.assertRaises(ValueError, No_of_cubes, 0, -1)
        self.assertRaises(ValueError, No_of_cubes, 1, 0)
