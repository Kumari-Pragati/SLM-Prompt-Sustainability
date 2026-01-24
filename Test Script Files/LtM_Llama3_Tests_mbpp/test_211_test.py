import unittest
from mbpp_211_code import count_Num

class TestCount_Num(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_Num(1), 1)
        self.assertEqual(count_Num(2), 2)
        self.assertEqual(count_Num(3), 4)
        self.assertEqual(count_Num(4), 8)
        self.assertEqual(count_Num(5), 16)

    def test_edge(self):
        self.assertEqual(count_Num(0), 1)
        self.assertEqual(count_Num(-1), 1)

    def test_edge2(self):
        self.assertEqual(count_Num(1), 1)
        self.assertEqual(count_Num(2), 2)
        self.assertEqual(count_Num(3), 4)
        self.assertEqual(count_Num(4), 8)
        self.assertEqual(count_Num(5), 16)

    def test_edge3(self):
        self.assertEqual(count_Num(10), 1024)

    def test_edge4(self):
        self.assertEqual(count_Num(20), 1048576)

    def test_edge5(self):
        self.assertEqual(count_Num(30), 1073741824)
