import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_check_greater_positive(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 6), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([10, 20, 30, 40, 50], 51), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([100, 200, 300, 400, 500], 501), 'Yes, the entered number is greater than those in the array')

    def test_check_greater_negative(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 0), 'No, entered number is less than those in the array')
        self.assertEqual(check_greater([10, 20, 30, 40, 50], -1), 'No, entered number is less than those in the array')
        self.assertEqual(check_greater([100, 200, 300, 400, 500], -501), 'No, entered number is less than those in the array')

    def test_check_greater_equal(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 5), 'Yes, the entered number is greater than or equal to those in the array')
        self.assertEqual(check_greater([10, 20, 30, 40, 50], 50), 'Yes, the entered number is greater than or equal to those in the array')
        self.assertEqual(check_greater([100, 200, 300, 400, 500], 500), 'Yes, the entered number is greater than or equal to those in the array')
