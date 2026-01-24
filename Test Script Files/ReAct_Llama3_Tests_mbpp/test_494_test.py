import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):

    def test_binary_to_integer_typical(self):
        self.assertEqual(binary_to_integer((1, 0, 1)), '5')

    def test_binary_to_integer_edge_case(self):
        self.assertEqual(binary_to_integer((1,)), '1')

    def test_binary_to_integer_edge_case2(self):
        self.assertEqual(binary_to_integer((0,)), '0')

    def test_binary_to_integer_edge_case3(self):
        self.assertEqual(binary_to_integer(()), '0')

    def test_binary_to_integer_edge_case4(self):
        self.assertEqual(binary_to_integer((1, 1, 1)), '3')

    def test_binary_to_integer_edge_case5(self):
        self.assertEqual(binary_to_integer((1, 1, 0, 1)), '6')

    def test_binary_to_integer_edge_case6(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 1)), '5')

    def test_binary_to_integer_edge_case7(self):
        self.assertEqual(binary_to_integer((0, 1, 0, 1)), '3')

    def test_binary_to_integer_edge_case8(self):
        self.assertEqual(binary_to_integer((1, 1, 1, 1)), '11')

    def test_binary_to_integer_edge_case9(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 0)), '2')

    def test_binary_to_integer_edge_case10(self):
        self.assertEqual(binary_to_integer((0, 0, 1, 1)), '5')

    def test_binary_to_integer_edge_case11(self):
        self.assertEqual(binary_to_integer((1, 1, 0, 0)), '2')

    def test_binary_to_integer_edge_case12(self):
        self.assertEqual(binary_to_integer((0, 1, 1, 1)), '7')

    def test_binary_to_integer_edge_case13(self):
        self.assertEqual(binary_to_integer((1, 0, 0, 1)), '5')

    def test_binary_to_integer_edge_case14(self):
        self.assertEqual(binary_to_integer((0, 0, 0, 1)), '1')

    def test_binary_to_integer_edge_case15(self):
        self.assertEqual(binary_to_integer((1, 1, 1, 0)), '6')

    def test_binary_to_integer_edge_case16(self):
        self.assertEqual(binary_to_integer((0, 1, 0, 0)), '2')

    def test_binary_to_integer_edge_case17(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 1)), '5')

    def test_binary_to_integer_edge_case18(self):
        self.assertEqual(binary_to_integer((0, 0, 1, 0)), '2')

    def test_binary_to_integer_edge_case19(self):
        self.assertEqual(binary_to_integer((1, 1, 0, 1)), '6')

    def test_binary_to_integer_edge_case20(self):
        self.assertEqual(binary_to_integer((0, 1, 1, 0)), '3')

    def test_binary_to_integer_edge_case21(self):
        self.assertEqual(binary_to_integer((1, 0, 0, 0)), '0')

    def test_binary_to_integer_edge_case22(self):
        self.assertEqual(binary_to_integer((0, 0, 0, 0)), '0')

    def test_binary_to_integer_edge_case23(self):
        self.assertEqual(binary_to_integer((1, 1, 1, 1, 1)), '15')

    def test_binary_to_integer_edge_case24(self):
        self.assertEqual(binary_to_integer((0, 1, 1, 1, 1)), '11')

    def test_binary_to_integer_edge_case25(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 1, 1)), '11')

    def test_binary_to_integer_edge_case26(self):
        self.assertEqual(binary_to_integer((0, 0, 1, 1, 1)), '11')

    def test_binary_to_integer_edge_case27(self):
        self.assertEqual(binary_to_integer((1, 1, 0, 1, 1)), '11')

    def test_binary_to_integer_edge_case28(self):
        self.assertEqual(binary_to_integer((0, 1, 0, 1, 1)), '11')

    def test_binary_to_integer_edge_case29(self):
        self.assertEqual(binary_to_integer((1, 0, 0, 1, 1)), '7')

    def test_binary_to_integer_edge_case30(self):
        self.assertEqual(binary_to_integer((0, 0, 0, 1, 1)), '7')
