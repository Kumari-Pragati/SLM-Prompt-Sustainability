import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_Min_Sum(1), 1)
        self.assertEqual(find_Min_Sum(2), 2)
        self.assertEqual(find_Min_Sum(3), 4)
        self.assertEqual(find_Min_Sum(4), 4)
        self.assertEqual(find_Min_Sum(5), 5)
        self.assertEqual(find_Min_Sum(6), 6)
        self.assertEqual(find_Min_Sum(7), 8)
        self.assertEqual(find_Min_Sum(8), 8)
        self.assertEqual(find_Min_Sum(9), 9)
        self.assertEqual(find_Min_Sum(10), 10)

    def test_edge(self):
        self.assertEqual(find_Min_Sum(0), 0)
        self.assertEqual(find_Min_Sum(1), 1)
        self.assertEqual(find_Min_Sum(2), 2)
        self.assertEqual(find_Min_Sum(3), 4)
        self.assertEqual(find_Min_Sum(4), 4)
        self.assertEqual(find_Min_Sum(5), 5)
        self.assertEqual(find_Min_Sum(6), 6)
        self.assertEqual(find_Min_Sum(7), 8)
        self.assertEqual(find_Min_Sum(8), 8)
        self.assertEqual(find_Min_Sum(9), 9)
        self.assertEqual(find_Min_Sum(10), 10)

    def test_complex(self):
        self.assertEqual(find_Min_Sum(11), 11)
        self.assertEqual(find_Min_Sum(12), 12)
        self.assertEqual(find_Min_Sum(13), 14)
        self.assertEqual(find_Min_Sum(14), 14)
        self.assertEqual(find_Min_Sum(15), 15)
        self.assertEqual(find_Min_Sum(16), 16)
        self.assertEqual(find_Min_Sum(17), 18)
        self.assertEqual(find_Min_Sum(18), 18)
        self.assertEqual(find_Min_Sum(19), 19)
        self.assertEqual(find_Min_Sum(20), 20)
