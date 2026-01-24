import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Swaps('abc', 'bca'), 1)

    def test_edge_case(self):
        self.assertEqual(min_Swaps('a', 'a'), 0)

    def test_boundary_case(self):
        self.assertEqual(min_Swaps('abc', ''), 'Not Possible')
        self.assertEqual(min_Swaps('', 'abc'), 'Not Possible')
        self.assertEqual(min_Swaps('', ''), 'Not Possible')

    def test_corner_case(self):
        self.assertEqual(min_Swaps('aaaa', 'aaaa'), 0)
        self.assertEqual(min_Swaps('abc', 'abc'), 'Not Possible')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, 'abc')
        with self.assertRaises(TypeError):
            min_Swaps('abc', 123)
        with self.assertRaises(TypeError):
            min_Swaps(123, 456)
