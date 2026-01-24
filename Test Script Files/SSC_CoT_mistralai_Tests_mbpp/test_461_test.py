import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(upper_ctr("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)
        self.assertEqual(upper_ctr("abcdefghijklmnopqrstuvwxyz"), 0)
        self.assertEqual(upper_ctr("ABCdeFGHIJKLMnOpQRSTUVwXYZ"), 10)

    def test_edge_cases(self):
        self.assertEqual(upper_ctr("A"), 1)
        self.assertEqual(upper_ctr("Z"), 1)
        self.assertEqual(upper_ctr("AAA"), 3)
        self.assertEqual(upper_ctr("ZZZ"), 3)

    def test_boundary_cases(self):
        self.assertEqual(upper_ctr(""), 0)
        self.assertEqual(upper_ctr("A "), 1)
        self.assertEqual(upper_ctr("Zz"), 1)
        self.assertEqual(upper_ctr("A1B2C3"), 3)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, upper_ctr, 123)
        self.assertRaises(TypeError, upper_ctr, [])
        self.assertRaises(TypeError, upper_ctr, None)
        self.assertRaises(TypeError, upper_ctr, (1, 2, 3))
