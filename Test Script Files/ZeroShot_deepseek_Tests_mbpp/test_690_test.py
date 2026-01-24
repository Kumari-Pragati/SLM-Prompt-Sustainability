import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_mul_consecutive_nums(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5]), [2, 6, 12, 20])
        self.assertEqual(mul_consecutive_nums([10, 20, 30, 40]), [200, 600, 1200])
        self.assertEqual(mul_consecutive_nums([1, 0, 3, 0, 5]), [0, 0, 0])
        self.assertEqual(mul_consecutive_nums([1]), [])
        self.assertEqual(mul_consecutive_nums([]), [])
