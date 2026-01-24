import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_multiply_list(self):
        self.assertEqual(multiply_list([1, 2, 3]), 6)
        self.assertEqual(multiply_list([-1, 2, 3]), -3)
        self.assertEqual(multiply_list([1, 2, 0]), 0)
        self.assertEqual(multiply_list([1, 2, -3]), -6)
        self.assertEqual(multiply_list([-1, -2, -3]), 6)
        self.assertEqual(multiply_list([1, 2, 3, 4]), 24)
        self.assertEqual(multiply_list([-1, -2, -3, -4]), 24)
        self.assertEqual(multiply_list([1, 2, 3, 4, 5]), 120)
        self.assertEqual(multiply_list([-1, -2, -3, -4, -5]), 120)
        self.assertEqual(multiply_list([1, 2, 3, 4, 5, 6]), 720)
        self.assertEqual(multiply_list([-1, -2, -3, -4, -5, -6]), 720)
