import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_div_of_nums(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 3), [2, 3, 4, 6, 8, 9])
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 5, 10), [10, 20, 30, 40, 50])
        self.assertEqual(div_of_nums([15, 25, 35, 45, 55], 5, 7), [15, 25, 35, 45, 55])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 1, 2), [1, 2, 3, 4, 5])
        self.assertEqual(div_of_nums([], 2, 3), [])
