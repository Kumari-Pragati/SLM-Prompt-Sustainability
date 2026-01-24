import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(end_num("Hello123"))

    def test_edge_case1(self):
        self.assertTrue(end_num("Hello"))

    def test_edge_case2(self):
        self.assertTrue(end_num("123456"))

    def test_edge_case3(self):
        self.assertFalse(end_num("HelloWorld"))

    def test_edge_case4(self):
        self.assertFalse(end_num(""))

    def test_edge_case5(self):
        self.assertFalse(end_num("Hello123abc"))

    def test_edge_case6(self):
        self.assertFalse(end_num("Hello123!"))

    def test_edge_case7(self):
        self.assertFalse(end_num("Hello123abc!"))

    def test_edge_case8(self):
        self.assertFalse(end_num("Hello123!abc"))

    def test_edge_case9(self):
        self.assertFalse(end_num("Hello123!abc!"))

    def test_edge_case10(self):
        self.assertFalse(end_num("Hello123!abc!@"))

    def test_edge_case11(self):
        self.assertFalse(end_num("Hello123!abc!@#"))

    def test_edge_case12(self):
        self.assertFalse(end_num("Hello123!abc!@#$"))

    def test_edge_case13(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^"))

    def test_edge_case14(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&"))

    def test_edge_case15(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*"))

    def test_edge_case16(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()"))

    def test_edge_case17(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]"))

    def test_edge_case18(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}"))

    def test_edge_case19(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|"))

    def test_edge_case20(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~"))

    def test_edge_case21(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`"))

    def test_edge_case22(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!"))

    def test_edge_case23(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@"))

    def test_edge_case24(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#"))

    def test_edge_case25(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#$"))

    def test_edge_case26(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#$%^"))

    def test_edge_case27(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#$%^&"))

    def test_edge_case28(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#$%^&*"))

    def test_edge_case29(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#$%^&*()"))

    def test_edge_case30(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#$%^&*()[]"))

    def test_edge_case31(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#$%^&*()[]{}"))

    def test_edge_case32(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#$%^&*()[]{}|"))

    def test_edge_case33(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#$%^&*()[]{}|~"))

    def test_edge_case34(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#$%^&*()[]{}|~`"))

    def test_edge_case35(self):
        self.assertFalse(end_num("Hello123!abc!@#$%^&*()[]{}|~`!@#$%^&*