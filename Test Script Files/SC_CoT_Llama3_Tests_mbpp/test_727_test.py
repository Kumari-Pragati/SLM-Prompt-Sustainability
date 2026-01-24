import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(remove_char("Hello World"), "HelloWorld")

    def test_edge_case(self):
        self.assertEqual(remove_char("Hello_World"), "HelloWorld")

    def test_edge_case2(self):
        self.assertEqual(remove_char("Hello123World"), "HelloWorld")

    def test_edge_case3(self):
        self.assertEqual(remove_char("Hello123World!"), "HelloWorld")

    def test_edge_case4(self):
        self.assertEqual(remove_char("Hello123World!@#"), "HelloWorld")

    def test_edge_case5(self):
        self.assertEqual(remove_char("Hello123World!@#$$"), "HelloWorld")

    def test_edge_case6(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*"), "HelloWorld")

    def test_edge_case7(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()"), "HelloWorld")

    def test_edge_case8(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}"), "HelloWorld")

    def test_edge_case9(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|"), "HelloWorld")

    def test_edge_case10(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}"), "HelloWorld")

    def test_edge_case11(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]"), "HelloWorld")

    def test_edge_case12(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}"), "HelloWorld")

    def test_edge_case13(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}|"), "HelloWorld")

    def test_edge_case14(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||"), "HelloWorld")

    def test_edge_case15(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||{}"), "HelloWorld")

    def test_edge_case16(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||{}[]"), "HelloWorld")

    def test_edge_case17(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||{}[]{}"), "HelloWorld")

    def test_edge_case18(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||{}[]{}|"), "HelloWorld")

    def test_edge_case19(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||{}[]{}||"), "HelloWorld")

    def test_edge_case20(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||{}[]{}||{}"), "HelloWorld")

    def test_edge_case21(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||{}[]{}||{}[]"), "HelloWorld")

    def test_edge_case22(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||{}[]{}||{}[]{}"), "HelloWorld")

    def test_edge_case23(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||{}[]{}||{}[]{}|"), "HelloWorld")

    def test_edge_case24(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||{}[]{}||{}[]{}||"), "HelloWorld")

    def test_edge_case25(self):
        self.assertEqual(remove_char("Hello123World!@#$%^&*()[]{}|{}[]{}||{}[]{}||{}[]{}||{}"), "HelloWorld")
