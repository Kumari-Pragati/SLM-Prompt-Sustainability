import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(smartNumber(1), [])

    def test_single_element(self):
        self.assertEqual(smartNumber(2), [2])

    def test_small_list(self):
        self.assertEqual(smartNumber(5), [2, 3, 5])

    def test_large_list(self, n=1000):
        self.assertEqual(smartNumber(n), sorted([i for i in range(2, 3001) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0]))

    def test_negative_input(self):
        self.assertRaises(IndexError, smartNumber, -1)

    def test_zero_input(self):
        self.assertRaises(IndexError, smartNumber, 0)

    def test_large_input(self, n=3001):
        self.assertRaises(IndexError, smartNumber, n)
