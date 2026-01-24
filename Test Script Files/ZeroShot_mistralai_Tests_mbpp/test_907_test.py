import unittest
from907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_lucky_num_1(self):
        self.assertEqual(lucky_num(1), [1])

    def test_lucky_num_2(self):
        self.assertEqual(lucky_num(2), [1, 3])

    def test_lucky_num_3(self):
        self.assertEqual(lucky_num(3), [1, 3, 5])

    def test_lucky_num_4(self):
        self.assertEqual(lucky_num(4), [1, 3, 5, 7])

    def test_lucky_num_5(self):
        self.assertEqual(lucky_num(5), [1, 3, 5, 7, 9])

    def test_lucky_num_6(self):
        self.assertEqual(lucky_num(6), [1, 3, 5, 7, 9, 11])

    def test_lucky_num_7(self):
        self.assertEqual(lucky_num(7), [1, 3, 5, 7, 9, 11, 13])

    def test_lucky_num_8(self):
        self.assertEqual(lucky_num(8), [1, 3, 5, 7, 9, 11, 13, 15])

    def test_lucky_num_9(self):
        self.assertEqual(lucky_num(9), [1, 3, 5, 7, 9, 11, 13, 15, 17])
