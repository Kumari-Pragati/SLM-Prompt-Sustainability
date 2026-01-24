import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(check_greater([5, 3, 9, 1], 4), 'No, entered number is less than those in the array')

    def test_edge_case(self):
        self.assertEqual(check_greater([], 5), 'No, entered number is less than those in the array')

    def test_boundary_case(self):
        self.assertEqual(check_greater([5, 3, 9, 1], 10), 'Yes, the entered number is greater than those in the array')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_greater('not a list', 5)
