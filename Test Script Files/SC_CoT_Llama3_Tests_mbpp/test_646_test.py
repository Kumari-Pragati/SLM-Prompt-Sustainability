import unittest
from mbpp_646_code import No_of_cubes

class TestNo_of_cubes(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(No_of_cubes(10, 5), 125)

    def test_edge_cases(self):
        self.assertEqual(No_of_cubes(0, 0), 0)
        self.assertEqual(No_of_cubes(1, 0), 1)
        self.assertEqual(No_of_cubes(1, 1), 1)
        self.assertEqual(No_of_cubes(-1, 0), 0)
        self.assertEqual(No_of_cubes(-1, 1), 0)

    def test_boundary_cases(self):
        self.assertEqual(No_of_cubes(5, 5), 0)
        self.assertEqual(No_of_cubes(5, 0), 0)
        self.assertEqual(No_of_cubes(0, 5), 0)

    def test_special_cases(self):
        self.assertEqual(No_of_cubes(10, 10), 0)
        self.assertEqual(No_of_cubes(-10, -10), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            No_of_cubes('a', 5)
        with self.assertRaises(TypeError):
            No_of_cubes(5, 'b')
