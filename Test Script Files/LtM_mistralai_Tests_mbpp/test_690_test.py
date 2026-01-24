import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(mul_consecutive_nums([1, 2, 3, 4]), [2*1, 3*2])
        self.assertListEqual(mul_consecutive_nums([5, 6, 7, 8]), [6*5, 7*6])

    def test_edge_cases(self):
        self.assertListEqual(mul_consecutive_nums([1]), [None])
        self.assertListEqual(mul_consecutive_nums([1, 2]), [None])
        self.assertListEqual(mul_consecutive_nums([1, 2, 3]), [2])
        self.assertListEqual(mul_consecutive_nums([1, 2, 3, 4, 5]), [2*1, 3*2, 4*3])

    def test_complex_cases(self):
        self.assertListEqual(mul_consecutive_nums([0, 0, 0]), [None])
        self.assertListEqual(mul_consecutive_nums([1, 0, 2]), [None, None, 2])
        self.assertListEqual(mul_consecutive_nums([-1, -2, -3]), [1, 2, 3])
        self.assertListEqual(mul_consecutive_nums([1, -2, 3]), [None, -2, 3])
