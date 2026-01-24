import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(min_Swaps('abc', 'bca'), 1)
        self.assertEqual(min_Swaps('123', '321'), 1)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(min_Swaps('', ''), 0)
        self.assertEqual(min_Swaps('a', 'a'), 0)
        self.assertEqual(min_Swaps('abc', 'abc'), 0)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(min_Swaps('abcd', 'dcba'), 2)
        self.assertEqual(min_Swaps('1234', '4321'), 2)
        self.assertEqual(min_Swaps('aaaa', 'aaaa'), 0)
        self.assertEqual(min_Swaps('abab', 'baba'), 1)

    # Test for invalid inputs
    def test_invalid_inputs(self):
        self.assertEqual(min_Swaps('abc', 'abcd'), "Not Possible")
        self.assertEqual(min_Swaps('123', '1234'), "Not Possible")
