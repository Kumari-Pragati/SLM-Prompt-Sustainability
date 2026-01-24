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
        self.assertEqual(sequence(4), 4)

    def test_sequence_5(self):
        self.assertEqual(sequence(5), 5)

    def test_sequence_6(self):
        self.assertEqual(sequence(6), 7)

    def test_sequence_7(self):
        self.assertEqual(sequence(7), 10)

    def test_sequence_8(self):
        self.assertEqual(sequence(8), 14)

    def test_sequence_9(self):
        self.assertEqual(sequence(9), 18)

    def test_sequence_10(self):
        self.assertEqual(sequence(10), 24)

    def test_sequence_11(self):
        self.assertEqual(sequence(11), 31)

    def test_sequence_12(self):
        self.assertEqual(sequence(12), 40)

    def test_sequence_13(self):
        self.assertEqual(sequence(13), 50)

    def test_sequence_14(self):
        self.assertEqual(sequence(14), 62)

    def test_sequence_15(self):
        self.assertEqual(sequence(15), 75)

    def test_sequence_16(self):
        self.assertEqual(sequence(16), 90)

    def test_sequence_17(self):
        self.assertEqual(sequence(17), 107)

    def test_sequence_18(self):
        self.assertEqual(sequence(18), 126)

    def test_sequence_19(self):
        self.assertEqual(sequence(19), 147)

    def test_sequence_20(self):
        self.assertEqual(sequence(20), 170)
