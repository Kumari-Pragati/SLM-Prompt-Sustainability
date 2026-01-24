import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_zero(self):
        self.assertEqual(cube_nums([0]), [0])

    def test_negative_numbers(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [1, 8, 27])

    def test_empty_list(self):
        self.assertEqual(cube_nums([]), [])

    def test_list_with_non_number(self):
        with self.assertRaises(TypeError):
            cube_nums([1, 'a', 3])
