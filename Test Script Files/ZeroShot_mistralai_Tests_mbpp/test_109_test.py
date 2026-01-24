import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(odd_Equivalent('', 10), 0)

    def test_all_zeros(self):
        self.assertEqual(odd_Equivalent('0' * 10, 10), 0)

    def test_all_ones(self):
        self.assertEqual(odd_Equivalent('1' * 10, 10), 10)

    def test_odd_length(self):
        self.assertEqual(odd_Equivalent('101', 3), 2)

    def test_even_length(self):
        self.assertEqual(odd_Equivalent('1010', 4), 1)

    def test_longer_string(self):
        self.assertEqual(odd_Equivalent('1010101', 7), 4)

    def test_shorter_string(self):
        self.assertEqual(odd_Equivalent('101', 5), 0)
