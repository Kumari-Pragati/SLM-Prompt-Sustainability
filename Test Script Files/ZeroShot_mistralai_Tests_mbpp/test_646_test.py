import unittest
from646_code import No_of_cubes

class TestNoOfCubes(unittest.TestCase):

    def test_no_of_cubes_with_positive_numbers(self):
        self.assertEqual(No_of_cubes(3, 1), 27)
        self.assertEqual(No_of_cubes(4, 2), 64)
        self.assertEqual(No_of_cubes(5, 3), 125)

    def test_no_of_cubes_with_zero(self):
        self.assertEqual(No_of_cubes(0, 0), 0)

    def test_no_of_cubes_with_negative_numbers(self):
        self.assertRaises(ValueError, No_of_cubes, -1, 0)
        self.assertRaises(ValueError, No_of_cubes, 0, -1)
        self.assertRaises(ValueError, No_of_cubes, -1, -1)
