import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_list([1, 2, 3]), 9)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([5]), 25)

    def test_large_list(self):
        self.assertEqual(count_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 100)

    def test_negative_numbers(self):
        self.assertEqual(count_list([-1, -2, -3]), 9)

    def test_mixed_numbers(self):
        self.assertEqual(count_list([1, -2, 3, -4]), 25)

    def test_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            count_list([1, 2, 'a', 4])
