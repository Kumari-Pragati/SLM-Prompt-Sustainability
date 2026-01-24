import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):
    def test_base_case_1(self):
        self.assertEqual(sequence(1), 1)

    def test_base_case_2(self):
        self.assertEqual(sequence(2), 1)

    def test_small_positive_numbers(self):
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 3)
        self.assertEqual(sequence(5), 5)

    def test_large_positive_numbers(self):
        self.assertEqual(sequence(10), 55)
        self.assertEqual(sequence(100), 354224848179261915075)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, sequence, -1)
        self.assertRaises(ValueError, sequence, 0)
