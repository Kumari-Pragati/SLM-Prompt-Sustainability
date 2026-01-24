import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_div_of_nums_typical(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3, 4), [3, 6, 9, 12])

    def test_div_of_nums_edge(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12, 12), [12])

    def test_div_of_nums_edge2(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 1, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_div_of_nums_invalid_input(self):
        with self.assertRaises(TypeError):
            div_of_nums("hello", 3, 4)

    def test_div_of_nums_invalid_input2(self):
        with self.assertRaises(TypeError):
            div_of_nums([1, 2, 3], "hello", 4)

    def test_div_of_nums_invalid_input3(self):
        with self.assertRaises(TypeError):
            div_of_nums([1, 2, 3], 3, "hello")
