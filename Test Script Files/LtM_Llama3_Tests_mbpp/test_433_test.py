import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(check_greater([1, 2, 3], 4), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([1, 2, 3], 1), 'No, entered number is less than those in the array')
        self.assertEqual(check_greater([1, 2, 3], 3), 'No, entered number is less than those in the array')

    def test_empty_input(self):
        self.assertEqual(check_greater([], 1), 'No, entered number is less than those in the array')

    def test_single_element_input(self):
        self.assertEqual(check_greater([1], 1), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([1], 2), 'No, entered number is less than those in the array')

    def test_edge_cases(self):
        self.assertEqual(check_greater([1, 2, 3], 2), 'No, entered number is less than those in the array')
        self.assertEqual(check_greater([1, 2, 3], 3), 'No, entered number is less than those in the array')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_greater(None, 1)
