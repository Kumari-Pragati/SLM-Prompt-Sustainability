import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):

    def test_count_Hexadecimal(self):
        self.assertEqual(count_Hexadecimal(10, 15), 2)
        self.assertEqual(count_Hexadecimal(10, 20), 3)
        self.assertEqual(count_Hexadecimal(10, 25), 4)
        self.assertEqual(count_Hexadecimal(10, 30), 5)
        self.assertEqual(count_Hexadecimal(10, 35), 6)
        self.assertEqual(count_Hexadecimal(10, 40), 7)
        self.assertEqual(count_Hexadecimal(10, 45), 8)
        self.assertEqual(count_Hexadecimal(10, 50), 9)
        self.assertEqual(count_Hexadecimal(10, 55), 10)
        self.assertEqual(count_Hexadecimal(10, 60), 11)
