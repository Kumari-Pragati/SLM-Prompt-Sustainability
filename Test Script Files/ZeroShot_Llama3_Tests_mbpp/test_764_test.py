import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):

    def test_number_ctr(self):
        self.assertEqual(number_ctr('123'), 3)
        self.assertEqual(number_ctr('abc'), 0)
        self.assertEqual(number_ctr('123abc'), 3)
        self.assertEqual(number_ctr(''), 0)
        self.assertEqual(number_ctr('123456789'), 9)
        self.assertEqual(number_ctr('abcdefg'), 0)
        self.assertEqual(number_ctr('1234567890'), 10)
