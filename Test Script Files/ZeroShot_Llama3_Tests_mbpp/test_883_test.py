import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_div_of_nums(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30], 2, 3), [6, 12, 18])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30], 3, 4), [12, 24])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30], 2, 5), [10])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30], 1, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30], 4, 5), [])
