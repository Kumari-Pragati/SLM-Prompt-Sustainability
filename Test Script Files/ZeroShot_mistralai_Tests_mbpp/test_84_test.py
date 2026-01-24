import unittest
from84_code import sequence

class TestSequence(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)

    def test_small_numbers(self):
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 3)
        self.assertEqual(sequence(5), 5)

    def test_large_numbers(self):
        self.assertEqual(sequence(10), 55)
        self.assertEqual(sequence(20), 677)
        self.assertEqual(sequence(30), 2039)
