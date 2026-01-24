import unittest
from mbpp_646_code import No_of_cubes

class TestNoOfCubes(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(No_of_cubes(10, 5), 27000)
        self.assertEqual(No_of_cubes(20, 10), 138240000)

    def test_edge_cases(self):
        self.assertEqual(No_of_cubes(0, 0), 0)
        self.assertEqual(No_of_cubes(10, 10), 0)

    def test_boundary_conditions(self):
        self.assertEqual(No_of_cubes(10, 11), 0)
        self.assertEqual(No_of_cubes(10, 0), 1000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            No_of_cubes("10", 5)
        with self.assertRaises(TypeError):
            No_of_cubes(10, "5")
        with self.assertRaises(TypeError):
            No_of_cubes("10", "5")
        with self.assertRaises(ValueError):
            No_of_cubes(-10, 5)
        with self.assertRaises(ValueError):
            No_of_cubes(10, -5)
