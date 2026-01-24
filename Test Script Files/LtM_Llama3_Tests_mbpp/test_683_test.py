import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):
    def test_true(self):
        self.assertTrue(sum_Square(5))

    def test_false(self):
        self.assertFalse(sum_Square(10))

    def test_edge_case(self):
        self.assertTrue(sum_Square(4))

    def test_edge_case2(self):
        self.assertFalse(sum_Square(15))

    def test_edge_case3(self):
        self.assertFalse(sum_Square(16))

    def test_edge_case4(self):
        self.assertTrue(sum_Square(17))

    def test_edge_case5(self):
        self.assertFalse(sum_Square(20))

    def test_edge_case6(self):
        self.assertFalse(sum_Square(21))

    def test_edge_case7(self):
        self.assertTrue(sum_Square(22))

    def test_edge_case8(self):
        self.assertFalse(sum_Square(23))

    def test_edge_case9(self):
        self.assertFalse(sum_Square(24))

    def test_edge_case10(self):
        self.assertTrue(sum_Square(25))

    def test_edge_case11(self):
        self.assertFalse(sum_Square(26))

    def test_edge_case12(self):
        self.assertFalse(sum_Square(27))

    def test_edge_case13(self):
        self.assertTrue(sum_Square(28))

    def test_edge_case14(self):
        self.assertFalse(sum_Square(29))

    def test_edge_case15(self):
        self.assertFalse(sum_Square(30))
