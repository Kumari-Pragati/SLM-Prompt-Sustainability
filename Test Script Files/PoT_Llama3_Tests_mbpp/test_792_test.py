import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_list([1, 2, 3]), 3)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([5]), 1)

    def test_large_list(self):
        self.assertEqual(count_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

    def test_negative_numbers(self):
        self.assertEqual(count_list([-1, -2, -3]), 3)

    def test_mixed_types(self):
        self.assertEqual(count_list([1, 'a', 3.5]), 3)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            count_list(123)
