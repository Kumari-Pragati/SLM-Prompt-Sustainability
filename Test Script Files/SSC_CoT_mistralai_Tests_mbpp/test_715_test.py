import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):
    def test_normal_input(self):
        self.assertTupleEqual(str_to_tuple('1, 2, 3, 4'), (1, 2, 3, 4))

    def test_empty_input(self):
        self.assertIsInstance(str_to_tuple(''), tuple)
        self.assertIsNone(str_to_tuple(''))

    def test_single_input(self):
        self.assertIsInstance(str_to_tuple('5'), tuple)
        self.assertEqual(str_to_tuple('5'), (5,))

    def test_no_comma_input(self):
        self.assertIsInstance(str_to_tuple('1 2 3'), tuple)
        self.assertEqual(str_to_tuple('1 2 3'), (1, 2, 3))

    def test_whitespace_input(self):
        self.assertIsInstance(str_to_tuple('  1,   2,    3   '), tuple)
        self.assertEqual(str_to_tuple('  1,   2,    3   '), (1, 2, 3))

    def test_negative_input(self):
        self.assertIsInstance(str_to_tuple('-1, 0, 1'), tuple)
        self.assertEqual(str_to_tuple('-1, 0, 1'), (-1, 0, 1))

    def test_leading_trailing_spaces_input(self):
        self.assertIsInstance(str_to_tuple(' 1, 2, 3  '), tuple)
        self.assertEqual(str_to_tuple(' 1, 2, 3  '), (1, 2, 3))

    def test_invalid_input(self):
        self.assertRaises(ValueError, str_to_tuple, 'x, y, z, a')
        self.assertRaises(ValueError, str_to_tuple, '1, 2, 3, a')
