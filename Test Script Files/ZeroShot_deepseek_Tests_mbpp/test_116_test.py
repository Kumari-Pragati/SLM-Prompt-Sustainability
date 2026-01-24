import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(tuple_to_int((1,)), 1)
        self.assertEqual(tuple_to_int((9,)), 9)

    def test_double_digit(self):
        self.assertEqual(tuple_to_int((1, 2)), 12)
        self.assertEqual(tuple_to_int((9, 9)), 99)

    def test_large_numbers(self):
        self.assertEqual(tuple_to_int((1, 2, 3, 4, 5)), 12345)
        self.assertEqual(tuple_to_int((9, 9, 9, 9, 9)), 99999)

    def test_negative_numbers(self):
        self.assertEqual(tuple_to_int((-1, -2)), -12)
        self.assertEqual(tuple_to_int((-9, -9)), -99)

    def test_mixed_numbers(self):
        self.assertEqual(tuple_to_int((1, 0, 2)), 102)
        self.assertEqual(tuple_to_int((-1, 0, -2)), -102)
