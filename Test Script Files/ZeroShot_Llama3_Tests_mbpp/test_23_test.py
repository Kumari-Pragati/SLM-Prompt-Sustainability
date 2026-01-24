import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_maximum_Sum(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 18)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]), 18)
        self.assertEqual(maximum_Sum([[-1, -2, -3], [4, 5, 6], [7, 8, 9]]), 18)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11]]), 18)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12]]), 18)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13]]), 18)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14]]), 18)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15]]), 18)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]), 18)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]), 18)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]), 18)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]), 19)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]), 20)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]]), 21)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]]), 22)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]]), 23)
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,