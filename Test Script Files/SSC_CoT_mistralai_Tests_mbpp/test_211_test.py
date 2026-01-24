import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_Num(1), 1)
        self.assertEqual(count_Num(2), 2)
        self.assertEqual(count_Num(3), 4)
        self.assertEqual(count_Num(4), 16)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Num(0), 0)
        self.assertEqual(count_Num(5), 64)
        self.assertEqual(count_Num(6), 256)
        self.assertEqual(count_Num(7), 1024)
        self.assertEqual(count_Num(8), 4096)

    def test_negative_input(self):
        self.assertRaises(ValueError, count_Num, -1)
        self.assertRaises(ValueError, count_Num, -2)
        self.assertRaises(ValueError, count_Num, -3)
