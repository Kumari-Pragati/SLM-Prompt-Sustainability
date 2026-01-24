import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_normal_input(self):
        self.assertTrue(end_num("hello123"))
        self.assertTrue(end_num("abcd4567"))
        self.assertTrue(end_num("1"))
        self.assertTrue(end_num("0"))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(end_num("abcdefghijklmnopqrstuvwxyz0"))
        self.assertTrue(end_num("ABCDEFGHIJKLMNOPQRSTUVWXYZ0"))
        self.assertTrue(end_num("!@#$%^&*()_+-=[]{};':\"<>,.?/0123456789"))
        self.assertTrue(end_num("0123456789"))
        self.assertTrue(end_num("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertTrue(end_num("0123456789!@#$%^&*()_+-=[]{};':\"<>,.?/"))

    def test_no_number(self):
        self.assertFalse(end_num("hello"))
        self.assertFalse(end_num("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(end_num("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertFalse(end_num("!@#$%^&*()_+-=[]{};':\"<>,.?"))
