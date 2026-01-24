import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_dig_let(self):
        self.assertEqual(dig_let('abc123'), (3, 3))
        self.assertEqual(dig_let('123abc'), (3, 3))
        self.assertEqual(dig_let('abc'), (3, 0))
        self.assertEqual(dig_let('123'), (0, 3))
        self.assertEqual(dig_let(''), (0, 0))
        self.assertEqual(dig_let('123abcABC'), (6, 3))
        self.assertEqual(dig_let('abc123ABC'), (3, 3))
        self.assertEqual(dig_let('123456'), (0, 6))
        self.assertEqual(dig_let('abcdef'), (6, 0))
        self.assertEqual(dig_let('1234567890'), (0, 10))
