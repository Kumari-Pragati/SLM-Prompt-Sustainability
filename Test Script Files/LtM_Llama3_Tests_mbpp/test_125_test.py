import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_length('00000', 5), 0)
        self.assertEqual(find_length('11111', 5), 5)
        self.assertEqual(find_length('01010', 5), 2)
        self.assertEqual(find_length('10101', 5), 2)
        self.assertEqual(find_length('00000', 0), 0)

    def test_edge(self):
        self.assertEqual(find_length('', 0), 0)
        self.assertEqual(find_length('0', 1), 1)
        self.assertEqual(find_length('1', 1), 1)
        self.assertEqual(find_length('000', 3), 0)
        self.assertEqual(find_length('111', 3), 3)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            find_length(None, 5)
        with self.assertRaises(TypeError):
            find_length('abc', None)
