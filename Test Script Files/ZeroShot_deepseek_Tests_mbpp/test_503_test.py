import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):

    def test_add_consecutive_nums(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [2, 3, 4, 5])
        self.assertEqual(add_consecutive_nums([10, 20, 30, 40]), [20, 30, 40])
        self.assertEqual(add_consecutive_nums([1]), [])
        self.assertEqual(add_consecutive_nums([]), [])
