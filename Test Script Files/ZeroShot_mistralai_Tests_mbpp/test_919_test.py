import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(multiply_list([]), 1)

    def test_single_item_list(self):
        self.assertEqual(multiply_list([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(multiply_list([1, 2, 3, 4, 5]), 120)

    def test_negative_numbers(self):
        self.assertEqual(multiply_list([-1, -2, -3, -4, -5]), 120)

    def test_zero(self):
        self.assertEqual(multiply_list([0, 1, 2, 3, 4]), 0)

    def test_floats(self):
        self.assertAlmostEqual(multiply_list([1.0, 2.0, 3.0]), 6.0)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            multiply_list([1, 2, "3", 4])
