import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits([1, 2, 3]), 6)
        self.assertEqual(sum_of_digits([10, 20, 30]), 60)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 60)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 66)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 72)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 78)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 90)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 96)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), 102)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), 108)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), 114)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 120)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), 126)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), 132)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]), 138)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), 144)
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9,