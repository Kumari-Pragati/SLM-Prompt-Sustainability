import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_min_swaps(self):
        self.assertEqual(min_Swaps('000000', '111111'), 0)
        self.assertEqual(min_Swaps('000001', '111110'), 1)
        self.assertEqual(min_Swaps('000011', '111101'), 2)
        self.assertEqual(min_Swaps('000111', '111000'), 2)
        self.assertEqual(min_Swaps('111111', '000000'), 0)
        self.assertEqual(min_Swaps('111110', '000001'), 1)
        self.assertEqual(min_Swaps('111101', '000011'), 2)
        self.assertEqual(min_Swaps('111000', '000111'), 2)
        self.assertEqual(min_Swaps('101010', '010101'), 2)
        self.assertEqual(min_Swaps('101101', '010010'), 2)
        self.assertEqual(min_Swaps('010101', '101010'), 2)
        self.assertEqual(min_Swaps('010010', '101101'), 2)
        self.assertEqual(min_Swaps('111111', '111111'), 0)
        self.assertEqual(min_Swaps('000000', '000000'), 0)
        self.assertEqual(min_Swaps('101010', '101010'), 0)
        self.assertEqual(min_Swaps('111111', '000000'), -1)
        self.assertEqual(min_Swaps('000000', '111111'), -1)
        self.assertEqual(min_Swaps('101010', '010101'), -1)
        self.assertEqual(min_Swaps('010101', '101010'), -1)
