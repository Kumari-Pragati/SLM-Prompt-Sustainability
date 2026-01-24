import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Swaps('0101', '1010'), 1)

    def test_boundary_conditions(self):
        self.assertEqual(min_Swaps('0', '1'), 1)
        self.assertEqual(min_Swaps('1', '0'), 1)
        self.assertEqual(min_Swaps('00', '00'), 0)
        self.assertEqual(min_Swaps('11', '11'), 0)

    def test_edge_cases(self):
        self.assertEqual(min_Swaps('0000', '1111'), -1)
        self.assertEqual(min_Swaps('01010', '10101'), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, '1010')
        with self.assertRaises(TypeError):
            min_Swaps('0101', 123)
        with self.assertRaises(TypeError):
            min_Swaps('0101', '10101010101010101010101010101010')
