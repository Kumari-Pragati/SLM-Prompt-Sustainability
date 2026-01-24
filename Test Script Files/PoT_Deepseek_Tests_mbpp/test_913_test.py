import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(end_num('abc1'))
        self.assertTrue(end_num('123'))
        self.assertTrue(end_num('abc123'))

    def test_edge_cases(self):
        self.assertFalse(end_num(''))
        self.assertFalse(end_num('abc'))
        self.assertFalse(end_num('123abc'))

    def test_corner_cases(self):
        self.assertTrue(end_num('1'))
        self.assertTrue(end_num('abc123def456'))
        self.assertFalse(end_num('abcdef'))
