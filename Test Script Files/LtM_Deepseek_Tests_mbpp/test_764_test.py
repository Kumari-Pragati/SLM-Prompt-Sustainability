import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(number_ctr("123abc"), 3)
        self.assertEqual(number_ctr("abc123"), 3)
        self.assertEqual(number_ctr("123456"), 6)

    def test_edge_conditions(self):
        self.assertEqual(number_ctr(""), 0)
        self.assertEqual(number_ctr("abc"), 0)
        self.assertEqual(number_ctr("1234567890"), 10)

    def test_complex_cases(self):
        self.assertEqual(number_ctr("1a2b3c4d5e6f7g8h9i0j"), 10)
        self.assertEqual(number_ctr("1234567890!@#$%^&*()"), 10)
        self.assertEqual(number_ctr("abcdefghijklmnopqrstuvwxyz"), 0)
