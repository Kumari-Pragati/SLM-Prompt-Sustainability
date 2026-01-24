import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(min_Swaps("abc", "abc"), 0)
        self.assertEqual(min_Swaps("abc", "def"), 3)
        self.assertEqual(min_Swaps("abc", "abcd"), 1)

    def test_edge(self):
        self.assertEqual(min_Swaps("a", "a"), 0)
        self.assertEqual(min_Swaps("a", "b"), 1)
        self.assertEqual(min_Swaps("a", "aa"), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, "abc")
        with self.assertRaises(TypeError):
            min_Swaps("abc", 123)

    def test_not_possible(self):
        self.assertEqual(min_Swaps("abc", "def"), "Not Possible")
        self.assertEqual(min_Swaps("abc", "defg"), "Not Possible")
