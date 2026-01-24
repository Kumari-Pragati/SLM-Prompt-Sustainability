import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):

    def test_empty_range(self):
        self.assertEqual(count_Hexadecimal(0, 0), 0)

    def test_single_digit_range(self):
        self.assertEqual(count_Hexadecimal(1, 9), 0)
        self.assertEqual(count_Hexadecimal(10, 15), 6)
        self.assertEqual(count_Hexadecimal(16, 19), 0)

    def test_two_digit_range(self):
        self.assertEqual(count_Hexadecimal(10, 19), 6)
        self.assertEqual(count_Hexadecimal(20, 29), 0)
        self.assertEqual(count_Hexadecimal(30, 39), 3)
        self.assertEqual(count_Hexadecimal(40, 49), 0)
        self.assertEqual(count_Hexadecimal(50, 59), 5)
        self.assertEqual(count_Hexadecimal(60, 69), 0)
        self.assertEqual(count_Hexadecimal(70, 79), 7)
        self.assertEqual(count_Hexadecimal(80, 89), 8)
        self.assertEqual(count_Hexadecimal(90, 99), 9)

    def test_three_digit_range(self):
        self.assertEqual(count_Hexadecimal(100, 199), 18)
        self.assertEqual(count_Hexadecimal(200, 299), 0)
        self.assertEqual(count_Hexadecimal(300, 399), 36)
        self.assertEqual(count_Hexadecimal(400, 499), 0)
        self.assertEqual(count_Hexadecimal(500, 599), 54)
        self.assertEqual(count_Hexadecimal(600, 699), 0)
        self.assertEqual(count_Hexadecimal(700, 799), 72)
        self.assertEqual(count_Hexadecimal(800, 899), 84)
        self.assertEqual(count_Hexadecimal(900, 999), 96)
