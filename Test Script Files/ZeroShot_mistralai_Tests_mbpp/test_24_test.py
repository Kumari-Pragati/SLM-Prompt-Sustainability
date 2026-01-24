import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(binary_to_decimal(""), 0)

    def test_zero(self):
        self.assertEqual(binary_to_decimal("0"), 0)

    def test_one(self):
        self.assertEqual(binary_to_decimal("1"), 1)

    def test_two(self):
        self.assertEqual(binary_to_decimal("10"), 2)

    def test_three(self):
        self.assertEqual(binary_to_decimal("11"), 3)

    def test_four(self):
        self.assertEqual(binary_to_decimal("100"), 4)

    def test_five(self):
        self.assertEqual(binary_to_decimal("101"), 5)

    def test_six(self):
        self.assertEqual(binary_to_decimal("110"), 6)

    def test_seven(self):
        self.assertEqual(binary_to_decimal("111"), 7)

    def test_eight(self):
        self.assertEqual(binary_to_decimal("1000"), 8)

    def test_nine(self):
        self.assertEqual(binary_to_decimal("1001"), 9)

    def test_ten(self):
        self.assertEqual(binary_to_decimal("1010"), 10)

    def test_eleven(self):
        self.assertEqual(binary_to_decimal("1011"), 11)

    def test_twelve(self):
        self.assertEqual(binary_to_decimal("1100"), 12)

    def test_thirteen(self):
        self.assertEqual(binary_to_decimal("1101"), 13)

    def test_fourteen(self):
        self.assertEqual(binary_to_decimal("1110"), 14)

    def test_fifteen(self):
        self.assertEqual(binary_to_decimal("1111"), 15)

    def test_negative_number(self):
        self.assertRaises(ValueError, binary_to_decimal, "-1")

    def test_non_binary_number(self):
        self.assertRaises(ValueError, binary_to_decimal, "123")
