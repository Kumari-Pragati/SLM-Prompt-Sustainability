import unittest
from mbpp_646_code import No_of_cubes

class TestNoOfCubes(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(No_of_cubes(5, 2), 27)
        self.assertEqual(No_of_cubes(10, 3), 5000)
        self.assertEqual(No_of_cubes(15, 5), 3375)

    def test_negative_numbers(self):
        self.assertEqual(No_of_cubes(-5, -2), -125)
        self.assertEqual(No_of_cubes(-10, -3), -1000)
        self.assertEqual(No_of_cubes(-15, -5), -3375)

    def test_zero(self):
        self.assertEqual(No_of_cubes(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(No_of_cubes(1, 1), 0)
        self.assertEqual(No_of_cubes(2, 1), 1)
        self.assertEqual(No_of_cubes(3, 1), 0)
