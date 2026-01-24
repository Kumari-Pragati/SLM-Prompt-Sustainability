import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(min_Swaps('1010', '0101'), 2)
        self.assertEqual(min_Swaps('1111', '0000'), 2)
        self.assertEqual(min_Swaps('0000', '1111'), 2)

    def test_edge_cases(self):
        self.assertEqual(min_Swaps('1000', '0100'), 1)
        self.assertEqual(min_Swaps('1111', '1111'), 0)
        self.assertEqual(min_Swaps('0000', '0000'), 0)

    def test_special_cases(self):
        self.assertEqual(min_Swaps('1010', '1010'), 1)
        self.assertEqual(min_Swaps('1111', '0000'), 2)
        self.assertEqual(min_Swaps('0000', '1111'), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Swaps('101', 'abc')
        with self.assertRaises(TypeError):
            min_Swaps('101', 123)
