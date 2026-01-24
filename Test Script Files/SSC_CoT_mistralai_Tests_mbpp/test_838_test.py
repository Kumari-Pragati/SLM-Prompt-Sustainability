import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(min_Swaps('0011', '1100'), 2)
        self.assertEqual(min_Swaps('1010', '1111'), 3)
        self.assertEqual(min_Swaps('0101', '1110'), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(min_Swaps('0', '1'), 0)
        self.assertEqual(min_Swaps('1', '0'), 0)
        self.assertEqual(min_Swaps('00', '11'), 0)
        self.assertEqual(min_Swaps('11', '00'), 0)
        self.assertEqual(min_Swaps('01', '10'), 1)
        self.assertEqual(min_Swaps('10', '01'), 1)
        self.assertEqual(min_Swaps('000', '111'), 3)
        self.assertEqual(min_Swaps('111', '000'), 3)
        self.assertEqual(min_Swaps('01010101', '11111111'), 6)
        self.assertEqual(min_Swaps('11111111', '01010101'), 6)

    def test_special_cases(self):
        self.assertEqual(min_Swaps('0000', '1111'), 4)
        self.assertEqual(min_Swaps('1111', '0000'), 4)
        self.assertEqual(min_Swaps('0000', '0000'), 0)
        self.assertEqual(min_Swaps('1111', '1111'), 0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, min_Swaps, '001', '110')
        self.assertRaises(ValueError, min_Swaps, '001', '11')
        self.assertRaises(ValueError, min_Swaps, '001', '')
        self.assertRaises(ValueError, min_Swaps, '', '110')
