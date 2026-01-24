import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(end_num("Hello123"))
        self.assertTrue(end_num("123456789"))
        self.assertTrue(end_num("abcd1234"))

    def test_edge_cases(self):
        self.assertTrue(end_num("1"))
        self.assertTrue(end_num("0"))
        self.assertTrue(end_num("1230"))
        self.assertTrue(end_num("123.456"))

    def test_boundary_cases(self):
        self.assertFalse(end_num("123"))
        self.assertFalse(end_num("12345"))
        self.assertFalse(end_num("1234567"))
        self.assertFalse(end_num("12345678"))

    def test_corner_cases(self):
        self.assertFalse(end_num("1_23"))
        self.assertFalse(end_num("123-456"))
        self.assertFalse(end_num("123.456"))
        self.assertFalse(end_num("123e456"))
        self.assertFalse(end_num("123f456"))
