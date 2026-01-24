import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(min_Swaps('abc', 'bca'), 1)
        self.assertEqual(min_Swaps('123', '321'), 1)
        self.assertEqual(min_Swaps('abcd', 'dcba'), 2)

    def test_edge_cases(self):
        self.assertEqual(min_Swaps('', ''), 0)
        self.assertEqual(min_Swaps('a', 'a'), 0)
        self.assertEqual(min_Swaps('ab', 'ab'), 0)

    def test_boundary_cases(self):
        self.assertEqual(min_Swaps('a'*10000, 'a'*10000), 0)
        self.assertEqual(min_Swaps('b'*10000, 'a'*10000), 5000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, 'abc')
        with self.assertRaises(TypeError):
            min_Swaps('abc', 123)
        with self.assertRaises(TypeError):
            min_Swaps(123, 456)
