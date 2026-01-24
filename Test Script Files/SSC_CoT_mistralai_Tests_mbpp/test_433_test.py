import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(check_greater([1, 2, 3], 4), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([5, 4, 3], 6), 'Yes, the entered number is greater than those in the array')

    def test_edge_cases(self):
        self.assertEqual(check_greater([], 1), 'No, entered number is less than those in the array')
        self.assertEqual(check_greater([1], 1), 'No, entered number is less than those in the array')
        self.assertEqual(check_greater([1, 1], 2), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([1, 1, 1], 2), 'Yes, the entered number is greater than those in the array')

    def test_boundary_conditions(self):
        self.assertEqual(check_greater([-1, -2, -3], -4), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([0, 0, 0], 1), 'Yes, the entered number is greater than those in the array')

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_greater, [1, 2, 3], 'a')
        self.assertRaises(TypeError, check_greater, ['1', '2', '3'], 4)
