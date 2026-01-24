import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_div_even_odd_typical(self):
        self.assertEqual(div_even_odd([2, 3, 4, 5]), 2/3)

    def test_div_even_odd_edge_case(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8]), 2/4)

    def test_div_even_odd_edge_case2(self):
        self.assertEqual(div_even_odd([2, 4, 6, 10]), 2/3)

    def test_div_even_odd_edge_case3(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10]), 2/3)

    def test_div_even_odd_edge_case4(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12]), 2/3)

    def test_div_even_odd_edge_case5(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14]), 2/3)

    def test_div_even_odd_edge_case6(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16]), 2/4)

    def test_div_even_odd_edge_case7(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16, 18]), 2/3)

    def test_div_even_odd_edge_case8(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 2/3)

    def test_div_even_odd_edge_case9(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]), 2/3)

    def test_div_even_odd_edge_case10(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]), 2/4)

    def test_div_even_odd_edge_case11(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]), 2/3)

    def test_div_even_odd_edge_case12(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]), 2/4)

    def test_div_even_odd_edge_case13(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]), 2/3)

    def test_div_even_odd_edge_case14(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]), 2/4)

    def test_div_even_odd_edge_case15(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]), 2/3)

    def test_div_even_odd_edge_case16(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]), 2/4)

    def test_div_even_odd_edge_case17(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]), 2/3)

    def test_div_even_odd_edge_case18(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8, 10, 12