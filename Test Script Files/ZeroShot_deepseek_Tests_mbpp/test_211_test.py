import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):

    def test_count_Num_with_1(self):
        self.assertEqual(count_Num(1), 1)

    def test_count_Num_with_2(self):
        self.assertEqual(count_Num(2), 2)

    def test_count_Num_with_3(self):
        self.assertEqual(count_Num(3), 4)

    def test_count_Num_with_4(self):
        self.assertEqual(count_Num(4), 8)

    def test_count_Num_with_5(self):
        self.assertEqual(count_Num(5), 16)

    def test_count_Num_with_6(self):
        self.assertEqual(count_Num(6), 32)

    def test_count_Num_with_7(self):
        self.assertEqual(count_Num(7), 64)

    def test_count_Num_with_8(self):
        self.assertEqual(count_Num(8), 128)

    def test_count_Num_with_9(self):
        self.assertEqual(count_Num(9), 256)

    def test_count_Num_with_10(self):
        self.assertEqual(count_Num(10), 512)
