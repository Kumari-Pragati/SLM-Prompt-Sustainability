import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):
    def test_true_sum_square(self):
        self.assertTrue(sum_Square(5))

    def test_false_sum_square(self):
        self.assertFalse(sum_Square(10))

    def test_edge_case_sum_square(self):
        self.assertTrue(sum_Square(4))

    def test_edge_case_sum_square2(self):
        self.assertFalse(sum_Square(15))

    def test_edge_case_sum_square3(self):
        self.assertFalse(sum_Square(16))

    def test_edge_case_sum_square4(self):
        self.assertTrue(sum_Square(17))

    def test_edge_case_sum_square5(self):
        self.assertFalse(sum_Square(20))

    def test_edge_case_sum_square6(self):
        self.assertFalse(sum_Square(21))

    def test_edge_case_sum_square7(self):
        self.assertTrue(sum_Square(22))

    def test_edge_case_sum_square8(self):
        self.assertFalse(sum_Square(25))

    def test_edge_case_sum_square9(self):
        self.assertFalse(sum_Square(26))

    def test_edge_case_sum_square10(self):
        self.assertTrue(sum_Square(28))
