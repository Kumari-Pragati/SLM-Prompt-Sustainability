import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):

    def test_hexagonal_num(self):
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 9)
        self.assertEqual(hexagonal_num(3), 21)
        self.assertEqual(hexagonal_num(4), 37)
        self.assertEqual(hexagonal_num(5), 57)
        self.assertEqual(hexagonal_num(6), 81)
        self.assertEqual(hexagonal_num(7), 109)
        self.assertEqual(hexagonal_num(8), 141)
        self.assertEqual(hexagonal_num(9), 177)
        self.assertEqual(hexagonal_num(10), 217)
