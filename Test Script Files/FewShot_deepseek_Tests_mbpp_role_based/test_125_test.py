import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_length('010101', 6), 2)

    def test_all_zeros(self):
        self.assertEqual(find_length('000000', 6), 6)

    def test_all_ones(self):
        self.assertEqual(find_length('111111', 6), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_length('0', 1), 0)
        self.assertEqual(find_length('1', 1), 0)

    def test_empty_string(self):
        self.assertEqual(find_length('', 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_length(123456, 'abc')
