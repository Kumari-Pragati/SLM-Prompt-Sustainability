import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(odd_Equivalent('', 10), 0)

    def test_all_zeros(self):
        self.assertEqual(odd_Equivalent('0' * 10, 10), 5)

    def test_all_ones(self):
        self.assertEqual(odd_Equivalent('1' * 10, 10), 10)

    def test_mixed_numbers(self):
        self.assertEqual(odd_Equivalent('0101010101', 10), 6)

    def test_string_shorter_than_n(self):
        self.assertEqual(odd_Equivalent('101', 5), 3)

    def test_string_longer_than_n(self):
        self.assertEqual(odd_Equivalent('101' * 11, 10), 10)
