import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(min_Swaps('0101', '1010'), 1)

    def test_edge_case(self):
        self.assertEqual(min_Swaps('0000', '1111'), 0)

    def test_boundary_case(self):
        self.assertEqual(min_Swaps('0', '1'), 1)
        self.assertEqual(min_Swaps('1', '0'), 1)
        self.assertEqual(min_Swaps('00', '11'), 0)
        self.assertEqual(min_Swaps('11', '00'), 0)

    def test_special_case(self):
        self.assertEqual(min_Swaps('010101', '101010'), 1)
        self.assertEqual(min_Swaps('111111', '000000'), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Swaps(1234, '1010')
        with self.assertRaises(TypeError):
            min_Swaps('0101', 1234)
        with self.assertRaises(TypeError):
            min_Swaps('0101', '10101')
        with self.assertRaises(TypeError):
            min_Swaps('01011', '1010')
