import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_div_of_nums_typical(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30], 2, 3), [2, 3, 4, 6, 8, 9, 10, 12, 15, 20, 25, 30])

    def test_div_of_nums_edge_cases(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30], 1, 3), [1, 3, 4, 6, 8, 9, 10, 12, 15, 20, 25, 30])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30], 3, 1), [3, 6, 9, 10, 12, 15, 20, 25, 30])

    def test_div_of_nums_special_cases(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30], 4, 5), [4, 5, 8, 10, 12, 15, 20, 25, 30])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30], 2, 2), [2, 4, 6, 8, 10, 12, 15, 20, 25, 30])

    def test_div_of_nums_invalid_inputs(self):
        with self.assertRaises(TypeError):
            div_of_nums('hello', 2, 3)
        with self.assertRaises(TypeError):
            div_of_nums([1, 2, 3], 'hello', 3)
        with self.assertRaises(TypeError):
            div_of_nums([1, 2, 3], 2, 'hello')
