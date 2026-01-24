import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):

    def test_is_abundant_true(self):
        self.assertTrue(is_abundant(12))

    def test_is_abundant_false(self):
        self.assertFalse(is_abundant(15))

    def test_is_abundant_edge_case(self):
        self.assertFalse(is_abundant(1))

    def test_is_abundant_edge_case2(self):
        self.assertFalse(is_abundant(2))

    def test_is_abundant_edge_case3(self):
        self.assertFalse(is_abundant(3))

    def test_is_abundant_edge_case4(self):
        self.assertFalse(is_abundant(4))

    def test_is_abundant_edge_case5(self):
        self.assertFalse(is_abundant(5))

    def test_is_abundant_edge_case6(self):
        self.assertFalse(is_abundant(6))

    def test_is_abundant_edge_case7(self):
        self.assertFalse(is_abundant(7))

    def test_is_abundant_edge_case8(self):
        self.assertFalse(is_abundant(8))

    def test_is_abundant_edge_case9(self):
        self.assertFalse(is_abundant(9))

    def test_is_abundant_edge_case10(self):
        self.assertFalse(is_abundant(10))

    def test_is_abundant_edge_case11(self):
        self.assertFalse(is_abundant(11))

    def test_is_abundant_edge_case12(self):
        self.assertFalse(is_abundant(12))

    def test_is_abundant_edge_case13(self):
        self.assertFalse(is_abundant(13))

    def test_is_abundant_edge_case14(self):
        self.assertFalse(is_abundant(14))

    def test_is_abundant_edge_case15(self):
        self.assertFalse(is_abundant(15))

    def test_is_abundant_edge_case16(self):
        self.assertFalse(is_abundant(16))

    def test_is_abundant_edge_case17(self):
        self.assertFalse(is_abundant(17))

    def test_is_abundant_edge_case18(self):
        self.assertFalse(is_abundant(18))

    def test_is_abundant_edge_case19(self):
        self.assertFalse(is_abundant(19))

    def test_is_abundant_edge_case20(self):
        self.assertFalse(is_abundant(20))
