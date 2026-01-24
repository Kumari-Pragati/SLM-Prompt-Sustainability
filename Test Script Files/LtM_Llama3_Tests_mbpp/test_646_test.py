import unittest
from mbpp_646_code import No_of_cubes

class TestNo_of_cubes(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(No_of_cubes(1, 0), 1)
        self.assertEqual(No_of_cubes(2, 0), 8)
        self.assertEqual(No_of_cubes(3, 0), 27)
        self.assertEqual(No_of_cubes(4, 0), 64)
        self.assertEqual(No_of_cubes(5, 0), 125)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(No_of_cubes(0, 0), 0)
        self.assertEqual(No_of_cubes(1, 1), 0)
        self.assertEqual(No_of_cubes(2, 2), 0)
        self.assertEqual(No_of_cubes(3, 3), 0)
        self.assertEqual(No_of_cubes(4, 4), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            No_of_cubes('a', 0)
        with self.assertRaises(TypeError):
            No_of_cubes(0, 'b')
        with self.assertRaises(TypeError):
            No_of_cubes('a', 'b')
