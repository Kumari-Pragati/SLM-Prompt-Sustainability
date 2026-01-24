import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):

    def test_count_num_1(self):
        self.assertEqual(count_Num(1), 1)

    def test_count_num_2(self):
        self.assertEqual(count_Num(2), 2)

    def test_count_num_3(self):
        self.assertEqual(count_Num(3), 4)

    def test_count_num_4(self):
        self.assertEqual(count_Num(4), 16)

    def test_count_num_5(self):
        self.assertEqual(count_Num(5), 64)
