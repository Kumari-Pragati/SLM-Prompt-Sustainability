import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSum_of_Inverse_Divisors(unittest.TestCase):

    def test_Sum_of_Inverse_Divisors(self):
        self.assertEqual(Sum_of_Inverse_Divisors(1, 1), 1.00)
        self.assertEqual(Sum_of_Inverse_Divisors(2, 3), 1.50)
        self.assertEqual(Sum_of_Inverse_Divisors(3, 6), 2.00)
        self.assertEqual(Sum_of_Inverse_Divisors(4, 10), 2.50)
        self.assertEqual(Sum_of_Inverse_Divisors(5, 12), 2.40)
        self.assertEqual(Sum_of_Inverse_Divisors(6, 15), 2.50)
        self.assertEqual(Sum_of_Inverse_Divisors(7, 18), 2.57)
        self.assertEqual(Sum_of_Inverse_Divisors(8, 21), 2.63)
        self.assertEqual(Sum_of_Inverse_Divisors(9, 24), 2.67)
        self.assertEqual(Sum_of_Inverse_Divisors(10, 27), 2.70)
