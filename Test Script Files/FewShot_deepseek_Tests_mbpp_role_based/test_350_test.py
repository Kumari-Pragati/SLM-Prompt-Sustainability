import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(minimum_Length('aabbbccc'), 0)

    def test_edge_case(self):
        self.assertEqual(minimum_Length(''), 0)

    def test_boundary_case(self):
        self.assertEqual(minimum_Length('a'), 1)

    def test_single_char_case(self):
        self.assertEqual(minimum_Length('aaaaa'), 5)

    def test_mixed_case(self):
        self.assertEqual(minimum_Length('abcabcabc'), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            minimum_Length(12345)

        with self.assertRaises(TypeError):
            minimum_Length(123.45)

        with self.assertRaises(TypeError):
            minimum_Length(None)

        with self.assertRaises(TypeError):
            minimum_Length([1, 2, 3])

        with self.assertRaises(TypeError):
            minimum_Length({'a': 1, 'b': 2})

        with self.assertRaises(TypeError):
            minimum_Length((1, 2, 3))
