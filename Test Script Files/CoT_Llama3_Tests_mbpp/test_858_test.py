import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(count_list([1, 2, 3]), 9)

    def test_list_with_duplicates(self):
        self.assertEqual(count_list([1, 2, 2, 3, 3, 3]), 9)

    def test_list_with_negative_numbers(self):
        self.assertEqual(count_list([-1, -2, -3]), 9)

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            count_list([1, 'a', 2.5])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            count_list('not a list')
