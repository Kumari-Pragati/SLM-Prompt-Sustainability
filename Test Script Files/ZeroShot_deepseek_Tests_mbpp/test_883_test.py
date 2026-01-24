import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_div_of_nums(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 5, 10), [20, 30, 40])
        self.assertEqual(div_of_nums([15, 25, 35, 45, 55], 5, 10), [30, 40])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [])
        self.assertEqual(div_of_nums([], 2, 3), [])
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 0, 10), [])
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 10, 0), [])
