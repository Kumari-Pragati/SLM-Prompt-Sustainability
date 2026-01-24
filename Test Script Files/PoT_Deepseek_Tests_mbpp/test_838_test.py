import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(min_Swaps('0101', '1010'), 1)
        self.assertEqual(min_Swaps('1110', '0001'), 2)
        self.assertEqual(min_Swaps('1111', '1111'), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_Swaps('', ''), 0)
        self.assertEqual(min_Swaps('0', '1'), -1)
        self.assertEqual(min_Swaps('0000', '1111'), 2)
        self.assertEqual(min_Swaps('00000', '11111'), 3)

    def test_corner_cases(self):
        self.assertEqual(min_Swaps('00001', '11110'), 2)
        self.assertEqual(min_Swaps('01010101', '10101010'), 2)
        self.assertEqual(min_Swaps('00000000', '11111111'), 4)
