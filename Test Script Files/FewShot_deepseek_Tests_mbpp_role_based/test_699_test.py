import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Swaps('abc', 'bca'), 1)

    def test_edge_case(self):
        self.assertEqual(min_Swaps('aaa', 'aaa'), 0)

    def test_boundary_case(self):
        self.assertEqual(min_Swaps('abc', ''), "Not Possible")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, 'abc')
