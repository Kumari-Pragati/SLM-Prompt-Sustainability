import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):

    def test_simple_uppercase(self):
        self.assertEqual(upper_ctr("ABC"), 3)
        self.assertEqual(upper_ctr("A"), 1)
        self.assertEqual(upper_ctr("Z"), 1)

    def test_mixed_case(self):
        self.assertEqual(upper_ctr("aBc"), 2)
        self.assertEqual(upper_ctr("AbCd"), 3)
        self.assertEqual(upper_ctr("Ab12Cd"), 3)

    def test_edge_cases(self):
        self.assertEqual(upper_ctr(""), 0)
        self.assertEqual(upper_ctr("A" * 100), 100)
        self.assertEqual(upper_ctr("Z" * 100), 100)
        self.assertEqual(upper_ctr("Aa"), 1)
        self.assertEqual(upper_ctr("Zz"), 1)
