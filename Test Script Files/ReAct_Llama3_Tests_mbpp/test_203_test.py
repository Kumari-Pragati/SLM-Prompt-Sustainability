import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    def test_hamming_distance_zero(self):
        self.assertEqual(hamming_Distance(0, 0), 0)

    def test_hamming_distance_one(self):
        self.assertEqual(hamming_Distance(1, 0), 1)

    def test_hamming_distance_two(self):
        self.assertEqual(hamming_Distance(2, 1), 1)

    def test_hamming_distance_three(self):
        self.assertEqual(hamming_Distance(3, 2), 1)

    def test_hamming_distance_four(self):
        self.assertEqual(hamming_Distance(4, 3), 1)

    def test_hamming_distance_five(self):
        self.assertEqual(hamming_Distance(5, 4), 1)

    def test_hamming_distance_six(self):
        self.assertEqual(hamming_Distance(6, 5), 1)

    def test_hamming_distance_seven(self):
        self.assertEqual(hamming_Distance(7, 6), 1)

    def test_hamming_distance_eight(self):
        self.assertEqual(hamming_Distance(8, 7), 1)

    def test_hamming_distance_nine(self):
        self.assertEqual(hamming_Distance(9, 8), 1)

    def test_hamming_distance_ten(self):
        self.assertEqual(hamming_Distance(10, 9), 1)

    def test_hamming_distance_large(self):
        self.assertEqual(hamming_Distance(100, 99), 1)

    def test_hamming_distance_negative(self):
        self.assertEqual(hamming_Distance(-1, 0), 1)

    def test_hamming_distance_negative2(self):
        self.assertEqual(hamming_Distance(-2, -1), 1)

    def test_hamming_distance_negative3(self):
        self.assertEqual(hamming_Distance(-3, -2), 1)

    def test_hamming_distance_negative4(self):
        self.assertEqual(hamming_Distance(-4, -3), 1)

    def test_hamming_distance_negative5(self):
        self.assertEqual(hamming_Distance(-5, -4), 1)

    def test_hamming_distance_negative6(self):
        self.assertEqual(hamming_Distance(-6, -5), 1)

    def test_hamming_distance_negative7(self):
        self.assertEqual(hamming_Distance(-7, -6), 1)

    def test_hamming_distance_negative8(self):
        self.assertEqual(hamming_Distance(-8, -7), 1)

    def test_hamming_distance_negative9(self):
        self.assertEqual(hamming_Distance(-9, -8), 1)

    def test_hamming_distance_negative10(self):
        self.assertEqual(hamming_Distance(-10, -9), 1)
