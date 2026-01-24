import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(2), 10)
        self.assertEqual(decimal_To_Binary(3), 11)
        self.assertEqual(decimal_To_Binary(4), 100)
        self.assertEqual(decimal_To_Binary(5), 101)
        self.assertEqual(decimal_To_Binary(6), 110)
        self.assertEqual(decimal_To_Binary(7), 111)
        self.assertEqual(decimal_To_Binary(8), 1000)
        self.assertEqual(decimal_To_Binary(9), 1001)
        self.assertEqual(decimal_To_Binary(10), 1010)
        self.assertEqual(decimal_To_Binary(11), 1011)
        self.assertEqual(decimal_To_Binary(12), 1100)
        self.assertEqual(decimal_To_Binary(13), 1101)
        self.assertEqual(decimal_To_Binary(14), 1110)
        self.assertEqual(decimal_To_Binary(15), 1111)
        self.assertEqual(decimal_To_Binary(16), 10000)
        self.assertEqual(decimal_To_Binary(255), 11111111)
        self.assertEqual(decimal_To_Binary(1023), 1111111111)
        self.assertEqual(decimal_To_Binary(1024), 10000000000)
        self.assertEqual(decimal_To_Binary(16777215), 1111111111111111)

    def test_negative_numbers(self):
        self.assertEqual(decimal_To_Binary(-1), '1' + bin(-1)[2:])
        self.assertEqual(decimal_To_Binary(-2), '10' + bin(-2)[2:])
        self.assertEqual(decimal_To_Binary(-3), '11' + bin(-3)[2:])
        self.assertEqual(decimal_To_Binary(-4), '100' + bin(-4)[2:])
        self.assertEqual(decimal_To_Binary(-5), '101' + bin(-5)[2:])
        self.assertEqual(decimal_To_Binary(-6), '110' + bin(-6)[2:])
        self.assertEqual(decimal_To_Binary(-7), '111' + bin(-7)[2:])
        self.assertEqual(decimal_To_Binary(-8), '1000' + bin(-8)[2:])
        self.assertEqual(decimal_To_Binary(-9), '1001' + bin(-9)[2:])
        self.assertEqual(decimal_To_Binary(-10), '1010' + bin(-10)[2:])
        self.assertEqual(decimal_To_Binary(-11), '1011' + bin(-11)[2:])
        self.assertEqual(decimal_To_Binary(-12), '1100' + bin(-12)[2:])
        self.assertEqual(decimal_To_Binary(-13), '1101' + bin(-13)[2:])
        self.assertEqual(decimal_To_Binary(-14), '1110' + bin(-14)[2:])
        self.assertEqual(decimal_To_Binary(-15), '1111' + bin(-15)[2:])
        self.assertEqual(decimal_To_Binary(-16), '10000' + bin(-16)[2:])
        self.assertEqual(decimal_To_Binary(-32767