import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_Num(1), 1)
        self.assertEqual(count_Num(2), 2)
        self.assertEqual(count_Num(3), 4)
        self.assertEqual(count_Num(4), 16)
        self.assertEqual(count_Num(5), 64)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Num(0), 0)
        self.assertEqual(count_Num(6), 1024)
        self.assertEqual(count_Num(7), 4096)
        self.assertEqual(count_Num(8), 16384)
        self.assertEqual(count_Num(9), 65536)
