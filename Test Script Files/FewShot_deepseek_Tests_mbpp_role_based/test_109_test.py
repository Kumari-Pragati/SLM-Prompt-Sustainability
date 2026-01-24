import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(odd_Equivalent('1011', 4), 3)

    def test_all_ones(self):
        self.assertEqual(odd_Equivalent('1111', 4), 4)

    def test_all_zeros(self):
        self.assertEqual(odd_Equivalent('0000', 4), 0)

    def test_empty_string(self):
        self.assertEqual(odd_Equivalent('', 0), 0)

    def test_negative_n(self):
        with self.assertRaises(IndexError):
            odd_Equivalent('1011', -1)

    def test_n_greater_than_length_of_s(self):
        self.assertEqual(odd_Equivalent('1011', 5), 3)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            odd_Equivalent(1011, 4)

    def test_non_integer_n(self):
        with self.assertRaises(TypeError):
            odd_Equivalent('1011', '4')
