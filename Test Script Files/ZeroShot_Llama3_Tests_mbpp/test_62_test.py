import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):

    def test_smallest_num(self):
        self.assertEqual(smallest_num([1, 2, 3, 4, 5]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(smallest_num([10, 20, 30, 40, 50]), 10)
        self.assertEqual(smallest_num([-10, -20, -30, -40, -50]), -50)
        self.assertEqual(smallest_num([0, 0, 0, 0, 0]), 0)
        self.assertEqual(smallest_num([-10, 0, 10, 20, 30]), -10)
        self.assertEqual(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(smallest_num([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]), -10)
