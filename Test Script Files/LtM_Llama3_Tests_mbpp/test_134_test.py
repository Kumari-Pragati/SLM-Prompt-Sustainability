import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 1), "EVEN")
        self.assertEqual(check_last([1, 3, 5, 7, 9], 5, 1), "ODD")
        self.assertEqual(check_last([2, 4, 6, 8, 10], 5, 1), "EVEN")
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 2), "EVEN")

    def test_edge(self):
        self.assertEqual(check_last([], 0, 1), "EVEN")
        self.assertEqual(check_last([1], 1, 1), "EVEN")
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 0), "EVEN")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            check_last("abc", 5, 1)
        with self.assertRaises(TypeError):
            check_last([1, 2, 3, 4, 5], "abc", 1)
        with self.assertRaises(TypeError):
            check_last([1, 2, 3, 4, 5], 5, "abc")
