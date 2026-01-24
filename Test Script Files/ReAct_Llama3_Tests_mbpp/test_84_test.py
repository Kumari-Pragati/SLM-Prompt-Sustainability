import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):
    def test_sequence_1(self):
        self.assertEqual(sequence(1), 1)

    def test_sequence_2(self):
        self.assertEqual(sequence(2), 1)

    def test_sequence_3(self):
        self.assertEqual(sequence(3), 2)

    def test_sequence_4(self):
        self.assertEqual(sequence(4), 3)

    def test_sequence_negative(self):
        with self.assertRaises(TypeError):
            sequence(-1)

    def test_sequence_non_integer(self):
        with self.assertRaises(TypeError):
            sequence(3.5)

    def test_sequence_large(self):
        self.assertEqual(sequence(100), 354224848179261915075)
