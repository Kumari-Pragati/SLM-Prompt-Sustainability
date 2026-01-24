import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 4), 1)
        self.assertEqual(find_remainder([1, 2, 3], 3, 5), 1)
        self.assertEqual(find_remainder([1, 2, 3], 3, 7), 3)

    def test_edge(self):
        self.assertEqual(find_remainder([], 0, 4), 0)
        self.assertEqual(find_remainder([1], 1, 4), 1)
        self.assertEqual(find_remainder([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 11), 10)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            find_remainder("abc", 3, 4)
        with self.assertRaises(TypeError):
            find_remainder([1, 2, 3], "abc", 4)
        with self.assertRaises(TypeError):
            find_remainder([1, 2, 3], 3, "abc")
