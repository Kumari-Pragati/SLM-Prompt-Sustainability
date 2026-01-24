import unittest
from mbpp_646_code import No_of_cubes

class TestNoOfCubes(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(No_of_cubes(10, 5), 27000)
        self.assertEqual(No_of_cubes(20, 10), 138240000)

    def test_edge_conditions(self):
        self.assertEqual(No_of_cubes(1, 1), 1)
        self.assertEqual(No_of_cubes(100, 100), 1000000000)

    def test_boundary_conditions(self):
        self.assertEqual(No_of_cubes(0, 0), 0)
        self.assertEqual(No_of_cubes(1000, 1), 1000000000)

    def test_complex_cases(self):
        self.assertEqual(No_of_cubes(1000, 500), 500000000000000)
        self.assertEqual(No_of_cubes(500, 250), 4218750000000000)
