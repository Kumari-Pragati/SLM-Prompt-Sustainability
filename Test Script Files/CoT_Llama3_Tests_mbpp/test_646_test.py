import unittest
from mbpp_646_code import No_of_cubes

class TestNo_of_cubes(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(No_of_cubes(5, 2), 27)
        self.assertEqual(No_of_cubes(10, 3), 1000)
        self.assertEqual(No_of_cubes(15, 5), 3375)

    def test_edge_cases(self):
        self.assertEqual(No_of_cubes(0, 0), 0)
        self.assertEqual(No_of_cubes(1, 1), 1)
        self.assertEqual(No_of_cubes(2, 2), 8)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            No_of_cubes('a', 2)
        with self.assertRaises(TypeError):
            No_of_cubes(5, 'b')

    def test_boundary_conditions(self):
        self.assertEqual(No_of_cubes(1, 1), 1)
        self.assertEqual(No_of_cubes(2, 2), 8)
        self.assertEqual(No_of_cubes(3, 3), 27)
