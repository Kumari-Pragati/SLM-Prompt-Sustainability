import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(frequency([1, 2, 3, 2, 1], 2), 3)
        self.assertEqual(frequency([], 1), 0)
        self.assertEqual(frequency([1], 1), 1)

    def test_edge_cases(self):
        self.assertEqual(frequency([1, -1], 1), 1)
        self.assertEqual(frequency([2147483647, -2147483648], -2147483648), 1)

    def test_complex(self):
        self.assertEqual(frequency([1, 2, 3, 2, 1, 2, 3, 2, 1], 2), 5)
        self.assertEqual(frequency([1000000000, 1000000000, 1000000000], 1000000000), 3)
