import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):

    def test_empty_range(self):
        self.assertListEqual(divisible_by_digits(0, 0), [])

    def test_single_number(self):
        self.assertListEqual(divisible_by_digits(1, 1), [1])

    def test_simple_range(self):
        self.assertListEqual(divisible_by_digits(1, 10), [2, 4, 6, 8, 9])

    def test_large_range(self):
        self.assertListEqual(divisible_by_digits(100, 200), [
            102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200
        ])

    def test_negative_numbers(self):
        self.assertListEqual(divisible_by_digits(-10, -1), [])
        self.assertListEqual(divisible_by_digits(-10, 0), [])
        self.assertListEqual(divisible_by_digits(0, -1), [])
        self.assertListEqual(divisible_by_digits(-10, -10), [])
