import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(upper_ctr("ABC"), 3)
        self.assertEqual(upper_ctr("aBc"), 2)
        self.assertEqual(upper_ctr("AbCdEfGhIjKlMnOpQrStUvWxYz"), 26)

    def test_edge_case(self):
        self.assertEqual(upper_ctr("A"), 1)
        self.assertEqual(upper_ctr("Z"), 1)
        self.assertEqual(upper_ctr(""), 0)
        self.assertEqual(upper_ctr(" "), 0)
        self.assertEqual(upper_ctr("AZ"), 2)

    def test_boundary_case(self):
        self.assertEqual(upper_ctr("AA"), 2)
        self.assertEqual(upper_ctr("ZY"), 2)
        self.assertEqual(upper_ctr("AZa"), 2)
        self.assertEqual(upper_ctr("Zy"), 1)
