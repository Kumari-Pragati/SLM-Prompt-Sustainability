import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_sub_list(self):
        self.assertEqual(sub_list([10, 20, 30], [5, 5, 5]), [5, 15, 25])
        self.assertEqual(sub_list([-10, 20, 30], [5, 5, 5]), [-15, 15, 25])
        self.assertEqual(sub_list([10, 20, 30], [10, 20, 30]), [0, 0, 0])
        self.assertEqual(sub_list([-10, 20, 30], [-10, 20, 30]), [0, 0, 0])
        self.assertEqual(sub_list([10, 20, 30], []), [10, 20, 30])
        self.assertEqual(sub_list([], [10, 20, 30]), [-10, -20, -30])
        self.assertEqual(sub_list([10, 20, 30], [10, 20, 30, 40]), [0, 0, 0, -10])
        self.assertEqual(sub_list([-10, 20, 30], [10, 20, 30, 40]), [-20, 0, 0, -10])
