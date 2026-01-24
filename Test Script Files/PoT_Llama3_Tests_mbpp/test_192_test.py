import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_String("Hello123"))

    def test_edge_case1(self):
        self.assertFalse(check_String("Hello"))

    def test_edge_case2(self):
        self.assertFalse(check_String("123"))

    def test_edge_case3(self):
        self.assertTrue(check_String("Hello123"))

    def test_edge_case4(self):
        self.assertFalse(check_String("Hello123456"))

    def test_edge_case5(self):
        self.assertFalse(check_String("Hello123abc"))

    def test_edge_case6(self):
        self.assertFalse(check_String("abc123"))

    def test_edge_case7(self):
        self.assertFalse(check_String("abc"))

    def test_edge_case8(self):
        self.assertFalse(check_String("123"))

    def test_edge_case9(self):
        self.assertFalse(check_String(""))

    def test_edge_case10(self):
        self.assertFalse(check_String("   "))
