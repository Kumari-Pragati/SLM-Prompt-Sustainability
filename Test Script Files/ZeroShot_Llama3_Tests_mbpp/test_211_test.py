import unittest
from mbpp_211_code import count_Num

class TestCount_Num(unittest.TestCase):

    def test_count_Num(self):
        self.assertEqual(count_Num(1), 1)
        self.assertEqual(count_Num(2), 2)
        self.assertEqual(count_Num(3), 3)
        self.assertEqual(count_Num(4), 7)
        self.assertEqual(count_Num(5), 15)
        self.assertEqual(count_Num(6), 31)
        self.assertEqual(count_Num(7), 63)
        self.assertEqual(count_Num(8), 127)
        self.assertEqual(count_Num(9), 255)
        self.assertEqual(count_Num(10), 511)

    def test_count_Num_edge_cases(self):
        self.assertRaises(TypeError, count_Num, 'a')
        self.assertRaises(TypeError, count_Num, None)
