import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_sub_list(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])
        self.assertEqual(sub_list([10, 20, 30], [5, 15, 25]), [5, 5, 5])
        self.assertEqual(sub_list([100, 200, 300], [10, 20, 30]), [90, 180, 270])
        self.assertEqual(sub_list([], []), [])
        self.assertEqual(sub_list([1], [1]), [])
        self.assertEqual(sub_list([1, 2, 3], [1, 2, 3]), [])
        self.assertEqual(sub_list([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(sub_list([], [1, 2, 3]), [])
