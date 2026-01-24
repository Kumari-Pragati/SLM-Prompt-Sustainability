import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(multiply_list([]), 1)

    def test_single_element_list(self):
        self.assertEqual(multiply_list([5]), 5)

    def test_two_element_list(self):
        self.assertEqual(multiply_list([2, 3]), 6)

    def test_three_element_list(self):
        self.assertEqual(multiply_list([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(multiply_list([-1, -2, -3]), -6)

    def test_zero_in_list(self):
        self.assertEqual(multiply_list([0, 1, 2]), 0)

    def test_large_numbers(self):
        self.assertEqual(multiply_list([100, 200, 300]), 600000)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            multiply_list([1, 'a', 3])
