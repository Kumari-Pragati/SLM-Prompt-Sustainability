import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(left_rotate("abc", 1), "bca")
        self.assertEqual(left_rotate("abcd", 2), "cdef")
        self.assertEqual(left_rotate("xyz", 0), "xyz")

    def test_edge_cases(self):
        self.assertEqual(left_rotate("", 2), "")
        self.assertEqual(left_rotate("a", 1), "b")
        self.assertEqual(left_rotate("abc", 3), "bca")
        self.assertEqual(left_rotate("abc", 0), "abc")

    def test_negative_d(self):
        with self.assertRaises(ValueError):
            left_rotate("abc", -1)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            left_rotate(123, 4)
