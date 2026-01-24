import unittest
from mbpp_646_code import No_of_cubes

class TestNoOfCubes(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(No_of_cubes(1, 1), 1)
        self.assertEqual(No_of_cubes(2, 2), 8)
        self.assertEqual(No_of_cubes(3, 3), 27)

    def test_edge_cases(self):
        self.assertEqual(No_of_cubes(0, 0), 0)
        self.assertEqual(No_of_cubes(1, 0), 1)
        self.assertEqual(No_of_cubes(1, 10), 1)
        self.assertEqual(No_of_cubes(10, 1), 1)

    def test_boundary_cases(self):
        self.assertEqual(No_of_cubes(1, 2), 1)
        self.assertEqual(No_of_cubes(2, 1), 8)
