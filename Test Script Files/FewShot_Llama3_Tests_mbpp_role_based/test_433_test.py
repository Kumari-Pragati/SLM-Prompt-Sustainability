import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_greater(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(check_greater(arr, 6), 'Yes, the entered number is greater than those in the array')

    def test_equal(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(check_greater(arr, 5), 'No, entered number is less than those in the array')

    def test_smaller(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(check_greater(arr, 0), 'No, entered number is less than those in the array')

    def test_empty_array(self):
        arr = []
        self.assertEqual(check_greater(arr, 1), 'No, entered number is less than those in the array')

    def test_single_element_array(self):
        arr = [5]
        self.assertEqual(check_greater(arr, 6), 'Yes, the entered number is greater than those in the array')
