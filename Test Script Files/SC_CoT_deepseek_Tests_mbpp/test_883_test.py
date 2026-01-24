import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 5, 2), [20, 40])

    def test_edge_case(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_boundary_case(self):
        self.assertEqual(div_of_nums([0], 1, 1), [0])
        self.assertEqual(div_of_nums([], 1, 1), [])

    def test_special_case(self):
        self.assertEqual(div_of_nums([15, 25, 35, 45], 5, 5), [15, 25, 35, 45])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            div_of_nums([10, 20, 30, 40], 'a', 2)
        with self.assertRaises(TypeError):
            div_of_nums([10, 20, 30, 40], 5, 'b')
        with self.assertRaises(TypeError):
            div_of_nums([10, 20, 30, 40], 'a', 'b')
        with self.assertRaises(ValueError):
            div_of_nums([10, 20, 30, 40], 0, 2)
        with self.assertRaises(ValueError):
            div_of_nums([10, 20, 30, 40], 5, 0)
