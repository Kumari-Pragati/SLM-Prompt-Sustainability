import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(number_ctr("123"), 3)
        self.assertEqual(number_ctr("0"), 1)
        self.assertEqual(number_ctr("12345"), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(number_ctr(""), 0)
        self.assertEqual(number_ctr("9"), 1)
        self.assertEqual(number_ctr("0123456789"), 10)
        self.assertEqual(number_ctr("A1B2C3"), 3)
        self.assertEqual(number_ctr("12345678901"), 11)

    def test_complex_input(self):
        self.assertEqual(number_ctr("1a2b3c4"), 3)
        self.assertEqual(number_ctr("123-456"), 3)
        self.assertEqual(number_ctr("123.456"), 1)
        self.assertEqual(number_ctr("123_456"), 1)
        self.assertEqual(number_ctr("123+456"), 1)
