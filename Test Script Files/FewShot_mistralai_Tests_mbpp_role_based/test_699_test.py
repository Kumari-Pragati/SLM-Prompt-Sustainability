import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_same_strings(self):
        self.assertEqual(min_Swaps("abcd", "abcd"), 0)

    def test_single_difference(self):
        self.assertEqual(min_Swaps("abcd", "acbd"), 1)

    def test_multiple_differences(self):
        self.assertEqual(min_Swaps("abcd", "efgh"), 4)

    def test_even_differences(self):
        self.assertEqual(min_Swaps("abcd", "acde"), 1)

    def test_odd_differences(self):
        self.assertEqual(min_Swaps("abcd", "acde"), "Not Possible")

    def test_empty_strings(self):
        self.assertEqual(min_Swaps("", ""), 0)

    def test_single_string(self):
        self.assertEqual(min_Swaps("a", "b"), "Not Possible")

    def test_different_lengths(self):
        self.assertEqual(min_Swaps("abcd", "abc"), "Not Possible")
