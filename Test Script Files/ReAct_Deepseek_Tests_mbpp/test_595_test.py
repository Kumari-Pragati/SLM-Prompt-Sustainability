import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Swaps('abc', 'bca'), 1)

    def test_edge_case_same_strings(self):
        self.assertEqual(min_Swaps('abc', 'abc'), 0)

    def test_edge_case_empty_strings(self):
        self.assertEqual(min_Swaps('', ''), 0)

    def test_edge_case_different_length_strings(self):
        self.assertEqual(min_Swaps('abc', 'abcd'), "Not Possible")

    def test_explicitly_handled_error_case(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, 'abc')
