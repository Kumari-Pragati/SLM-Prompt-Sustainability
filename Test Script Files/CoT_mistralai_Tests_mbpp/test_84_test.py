import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)

    def test_positive_numbers(self):
        for n in range(3, 11):
            self.assertEqual(sequence(n), sequence(sequence(n-1)) + sequence(n-sequence(n-1)))

    def test_large_number(self):
        self.assertEqual(sequence(100), sequence(sequence(99)) + sequence(99 - sequence(99)))

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sequence(-1)

    def test_zero(self):
        with self.assertRaises(ValueError):
            sequence(0)

    def test_floating_point(self):
        with self.assertRaises(TypeError):
            sequence(3.14)
