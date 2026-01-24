import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_edge_case(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [-1, -8, -27])

    def test_empty_input(self):
        self.assertEqual(cube_nums([]), [])

    def test_single_element_input(self):
        self.assertEqual(cube_nums([5]), [125])

    def test_negative_input(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [-1, -8, -27])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            cube_nums([1, 2, '3'])

    def test_mixed_type_input(self):
        with self.assertRaises(TypeError):
            cube_nums([1, 2, 3, '4', 5])
