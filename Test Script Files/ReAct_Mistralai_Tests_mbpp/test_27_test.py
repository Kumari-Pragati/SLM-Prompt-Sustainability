import unittest
from mbpp_27_code import remove

class TestRemoveFunction(unittest.TestCase):

    def test_empty_list(self):
        result = remove([])
        self.assertEqual(result, [])

    def test_single_element_list(self):
        result = remove(['A'])
        self.assertEqual(result, ['A'])

    def test_list_with_numbers(self):
        result = remove([1, 'A', 3, 'B', 5])
        self.assertEqual(result, ['A', 'B'])

    def test_list_with_only_numbers(self):
        result = remove([1, 2, 3, 4, 5])
        self.assertEqual(result, [])

    def test_list_with_leading_numbers(self):
        result = remove([1, 'A', 2, 'B', 3])
        self.assertEqual(result, ['A', 'B'])

    def test_list_with_trailing_numbers(self):
        result = remove(['A', 1, 'B', 2])
        self.assertEqual(result, ['A', 'B'])

    def test_list_with_numbers_in_middle(self):
        result = remove(['A', 1, 'B', 2, 'C'])
        self.assertEqual(result, ['A', 'C'])

    def test_list_with_only_digits(self):
        result = remove(['123', '456', '789'])
        self.assertEqual(result, [])

    def test_list_with_empty_string(self):
        result = remove(['', 'A', 'B'])
        self.assertEqual(result, ['A', 'B'])

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            remove([1, 2, 3, 'A'])
