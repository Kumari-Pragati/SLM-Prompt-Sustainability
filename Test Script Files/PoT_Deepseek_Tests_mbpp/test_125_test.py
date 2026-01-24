import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_length('01010101', 8), 4)

    def test_all_zeros(self):
        self.assertEqual(find_length('00000000', 8), 8)

    def test_all_ones(self):
        self.assertEqual(find_length('11111111', 8), 0)

    def test_boundary_case(self):
        self.assertEqual(find_length('0', 1), 0)

    def test_empty_string(self):
        self.assertEqual(find_length('', 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_length(123456, 'abc')
