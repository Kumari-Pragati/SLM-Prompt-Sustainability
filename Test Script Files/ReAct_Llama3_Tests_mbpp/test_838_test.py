import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Swaps('101010', '010101'), 2)

    def test_edge_case1(self):
        self.assertEqual(min_Swaps('111111', '000000'), 2)

    def test_edge_case2(self):
        self.assertEqual(min_Swaps('000000', '111111'), 2)

    def test_edge_case3(self):
        self.assertEqual(min_Swaps('101010', '101010'), 0)

    def test_edge_case4(self):
        self.assertEqual(min_Swaps('111111', '111111'), 0)

    def test_edge_case5(self):
        self.assertEqual(min_Swaps('000000', '000000'), 0)

    def test_error_case1(self):
        self.assertEqual(min_Swaps('1010', '1010'), -1)

    def test_error_case2(self):
        self.assertEqual(min_Swaps('1010', '0101'), -1)
