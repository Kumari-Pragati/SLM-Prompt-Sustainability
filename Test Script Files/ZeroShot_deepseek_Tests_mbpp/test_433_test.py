import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_check_greater(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 6), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 5), 'No, entered number is less than those in the array')
        self.assertEqual(check_greater([10, 20, 30, 40, 50], 25), 'No, entered number is less than those in the array')
        self.assertEqual(check_greater([10, 20, 30, 40, 50], 55), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([], 5), 'No, entered number is less than those in the array')
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 0), 'No, entered number is less than those in the array')
