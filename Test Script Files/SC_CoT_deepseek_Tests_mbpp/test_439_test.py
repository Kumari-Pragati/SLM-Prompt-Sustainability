import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5]), 12345)

    def test_single_digit(self):
        self.assertEqual(multiple_to_single([5]), 5)

    def test_empty_list(self):
        self.assertEqual(multiple_to_single([]), 0)

    def test_large_number(self):
        self.assertEqual(multiple_to_single(list(range(1, 10001))), 123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899)

    def test_negative_numbers(self):
        self.assertEqual(multiple_to_single([-1, -2, -3, -4, -5]), -12345)

    def test_mixed_numbers(self):
        self.assertEqual(multiple_to_single([1, 2, -3, 4, -5]), 12-34-5)

    def test_float_numbers(self):
        with self.assertRaises(ValueError):
            multiple_to_single([1.1, 2.2, 3.3])
