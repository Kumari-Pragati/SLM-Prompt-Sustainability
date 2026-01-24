import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_even_swaps(self):
        self.assertEqual(min_Swaps('0101', '1010'), 2)
        self.assertEqual(min_Swaps('1110', '0001'), 2)

    def test_odd_swaps(self):
        self.assertEqual(min_Swaps('0101', '1011'), 3)
        self.assertEqual(min_Swaps('1110', '0000'), -1)

    def test_all_same(self):
        self.assertEqual(min_Swaps('0000', '0000'), 0)
        self.assertEqual(min_Swaps('1111', '1111'), 0)

    def test_empty_strings(self):
        self.assertEqual(min_Swaps('', ''), 0)

    def test_different_lengths(self):
        self.assertEqual(min_Swaps('01010', '10101'), -1)
