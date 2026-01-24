import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(min_Swaps('abc', 'abc'), 0)
        self.assertEqual(min_Swaps('abc', 'acb'), 1)
        self.assertEqual(min_Swaps('abcd', 'dcba'), 2)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(min_Swaps('', ''), 0)
        self.assertEqual(min_Swaps('a', 'a'), 0)
        self.assertEqual(min_Swaps('ab', 'ab'), 0)
        self.assertEqual(min_Swaps('abc', 'cba'), 2)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(min_Swaps('abcde', 'edcba'), 3)
        self.assertEqual(min_Swaps('aaaaa', 'aaaaa'), 0)
        self.assertEqual(min_Swaps('abc', 'def'), 'Not Possible')
