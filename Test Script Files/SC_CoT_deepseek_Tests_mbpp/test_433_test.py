import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_greater([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 10),
                         'Yes, the entered number is greater than those in the array')

    def test_edge_case_greater(self):
        self.assertEqual(check_greater([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 100),
                         'Yes, the entered number is greater than those in the array')

    def test_edge_case_smaller(self):
        self.assertEqual(check_greater([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], -1),
                         'No, entered number is less than those in the array')

    def test_boundary_case_greater(self):
        self.assertEqual(check_greater([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 5),
                         'Yes, the entered number is greater than those in the array')

    def test_boundary_case_smaller(self):
        self.assertEqual(check_greater([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 3),
                         'No, entered number is less than those in the array')

    def test_invalid_input_empty_list(self):
        with self.assertRaises(IndexError):
            check_greater([], 10)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            check_greater("not a list", 10)
