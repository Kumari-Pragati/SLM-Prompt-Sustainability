import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):

    def test_tup_string(self):
        self.assertEqual(tup_string(('H', 'e', 'l', 'l', 'o')), 'Hello')
        self.assertEqual(tup_string(('W', 'o', 'r', 'l', 'd')), 'World')
        self.assertEqual(tup_string(('1', '2', '3', '4', '5')), '12345')
        self.assertEqual(tup_string(()), '')
