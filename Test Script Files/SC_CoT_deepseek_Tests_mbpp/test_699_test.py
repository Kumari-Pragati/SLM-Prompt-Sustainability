import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Swaps('abc', 'bca'), 1)

    def test_edge_case(self):
        self.assertEqual(min_Swaps('', ''), 0)

    def test_boundary_case(self):
        self.assertEqual(min_Swaps('a', 'a'), 0)
        self.assertEqual(min_Swaps('ab', 'ba'), 1)

    def test_corner_case(self):
        self.assertEqual(min_Swaps('abc', 'cab'), 1)
        self.assertEqual(min_Swaps('abc', 'xyz'), 'Not Possible')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, 'abc')
        with self.assertRaises(TypeError):
            min_Swaps('abc', 123)
