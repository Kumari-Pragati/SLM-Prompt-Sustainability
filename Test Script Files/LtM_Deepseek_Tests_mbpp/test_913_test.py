import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):

    def test_simple_cases(self):
        self.assertTrue(end_num("hello1"))
        self.assertTrue(end_num("123"))
        self.assertTrue(end_num("abc9"))

    def test_edge_conditions(self):
        self.assertFalse(end_num(""))
        self.assertFalse(end_num(" "))
        self.assertFalse(end_num("no_numbers"))

    def test_complex_cases(self):
        self.assertTrue(end_num("123456789"))
        self.assertFalse(end_num("1234567890"))
        self.assertTrue(end_num("0"))
