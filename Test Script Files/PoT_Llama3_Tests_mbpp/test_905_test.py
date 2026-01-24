import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_of_square(2), 2)

    def test_edge_case(self):
        self.assertEqual(sum_of_square(0), 0)

    def test_edge_case2(self):
        self.assertEqual(sum_of_square(1), 1)

    def test_edge_case3(self):
        self.assertEqual(sum_of_square(-1), 0)

    def test_edge_case4(self):
        self.assertEqual(sum_of_square(2.5), 0)

    def test_edge_case5(self):
        self.assertEqual(sum_of_square('a'), 0)

    def test_edge_case6(self):
        self.assertEqual(sum_of_square(None), 0)

    def test_edge_case7(self):
        self.assertEqual(sum_of_square(3.5), 0)

    def test_edge_case8(self):
        self.assertEqual(sum_of_square(-2.5), 0)

    def test_edge_case9(self):
        self.assertEqual(sum_of_square('b'), 0)

    def test_edge_case10(self):
        self.assertEqual(sum_of_square(None), 0)
