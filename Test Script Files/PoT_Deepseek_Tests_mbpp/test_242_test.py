import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_charac('hello'), 5)
        self.assertEqual(count_charac('world'), 5)
        self.assertEqual(count_charac(''), 0)

    def test_edge_cases(self):
        self.assertEqual(count_charac('a'*10000), 10000)
        self.assertEqual(count_charac('b'*10001), 10001)

    def test_corner_cases(self):
        self.assertEqual(count_charac('!@#$%^&*()'), 10)
        self.assertEqual(count_charac('1234567890'), 10)
        self.assertEqual(count_charac(' '), 1)
