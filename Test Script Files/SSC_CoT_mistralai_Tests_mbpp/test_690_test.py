import unittest
from mbpp_690_code import zip

from690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_typical_input(self):
        self.assertListEqual(mul_consecutive_nums([1, 2, 3, 4, 5]), [2*1, 3*2, 4*3, 5*4])

    def test_edge_cases(self):
        self.assertListEqual(mul_consecutive_nums([1]), [None])
        self.assertListEqual(mul_consecutive_nums([1, 2]), [None])
        self.assertListEqual(mul_consecutive_nums([1, 2, 3]), [2])
        self.assertListEqual(mul_consecutive_nums([1, 2, 3, 4, 5, 6]), [5*4, 6*5])

    def test_empty_list(self):
        self.assertListEqual(mul_consecutive_nums([]), [])

    def test_single_element_list(self):
        self.assertListEqual(mul_consecutive_nums([1]), [None])

    def test_negative_numbers(self):
        self.assertListEqual(mul_consecutive_nums([-1, -2, -3]), [2*1, 3*2, -3])

    def test_floats(self):
        self.assertListEqual(mul_consecutive_nums([1.1, 2.2, 3.3]), [2.2*1.1, 3.3*2.2])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            mul_consecutive_nums([1, 'a', 3])
