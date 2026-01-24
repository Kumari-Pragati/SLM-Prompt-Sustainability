import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(min_Swaps('000', '111'), 0)
        self.assertEqual(min_Swaps('101', '010'), 1)
        self.assertEqual(min_Swaps('110000', '101100'), 2)

    def test_edge_cases(self):
        self.assertEqual(min_Swaps('', ''), 0)
        self.assertEqual(min_Swaps('0', '1'), -1)
        self.assertEqual(min_Swaps('01', '10'), 1)
        self.assertEqual(min_Swaps('000', '11111'), 4)
        self.assertEqual(min_Swaps('111111', '000000'), 4)
        self.assertEqual(min_Swaps('000000', '1111111'), -1)

    def test_complex_cases(self):
        self.assertEqual(min_Swaps('010101', '101010'), 2)
        self.assertEqual(min_Swaps('01010101', '10101010'), 4)
        self.assertEqual(min_Swaps('0101010101', '1010101010'), 6)
        self.assertEqual(min_Swaps('010101010101', '101010101010'), 8)
