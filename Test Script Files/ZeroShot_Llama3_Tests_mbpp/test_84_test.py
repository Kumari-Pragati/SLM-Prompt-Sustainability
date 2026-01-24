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

    def test_sequence_5(self):
        self.assertEqual(sequence(5), 5)

    def test_sequence_6(self):
        self.assertEqual(sequence(6), 8)

    def test_sequence_7(self):
        self.assertEqual(sequence(7), 13)

    def test_sequence_8(self):
        self.assertEqual(sequence(8), 21)

    def test_sequence_9(self):
        self.assertEqual(sequence(9), 34)

    def test_sequence_10(self):
        self.assertEqual(sequence(10), 55)
