import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):

    def test_square_normal(self):
        self.assertEqual(square_nums([1, 2, 3, 4]), [1, 4, 9, 16])

    def test_square_negative(self):
        self.assertEqual(square_nums([-1, -2, -3]), [1, 4, 9])

    def test_square_zero(self):
        self.assertEqual(square_nums([0]), [0])

    def test_square_float(self):
        self.assertListEqual(square_nums([3.14, 2.718]), [9.8596, 7.284])

    def test_square_empty_list(self):
        self.assertEqual(square_nums([]), [])

    def test_square_string(self):
        with self.assertRaises(TypeError):
            square_nums(['a', 'b', 'c'])
