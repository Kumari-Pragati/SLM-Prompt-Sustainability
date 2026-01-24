import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):

    def test_sum_elements(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)
        self.assertEqual(sum_elements((1, 2, 3, 4)), 10)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5)), 15)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5, 6)), 21)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5, 6, 7)), 28)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5, 6, 7, 8)), 36)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5, 6, 7, 8, 9)), 45)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), 55)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)), 66)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)), 78)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)), 91)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)), 105)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)), 120)

    def test_sum_elements_empty(self):
        self.assertEqual(sum_elements(()), 0)

    def test_sum_elements_single(self):
        self.assertEqual(sum_elements((1,)), 1)

    def test_sum_elements_negative(self):
        self.assertEqual(sum_elements((-1, 2, 3)), 4)
        self.assertEqual(sum_elements((-1, -2, 3)), 0)
        self.assertEqual(sum_elements((-1, -2, -3)), -6)
