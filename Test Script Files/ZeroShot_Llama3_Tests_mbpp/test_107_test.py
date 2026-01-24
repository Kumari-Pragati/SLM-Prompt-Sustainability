import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):

    def test_count_Hexadecimal(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)
        self.assertEqual(count_Hexadecimal(10, 20), 10)
        self.assertEqual(count_Hexadecimal(10, 25), 14)
        self.assertEqual(count_Hexadecimal(1, 10), 0)
        self.assertEqual(count_Hexadecimal(1, 1), 0)
        self.assertEqual(count_Hexadecimal(15, 15), 1)
        self.assertEqual(count_Hexadecimal(10, 10), 1)
        self.assertEqual(count_Hexadecimal(10, 100), 25)
