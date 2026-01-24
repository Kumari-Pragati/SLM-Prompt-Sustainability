import unittest
from mbpp_22_code import find_first_duplicate

class TestFindFirstDuplicate(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_first_duplicate([]), -1)

    def test_single_element(self):
        self.assertEqual(find_first_duplicate([1]), -1)

    def test_no_duplicates(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5]), -1)

    def test_duplicate_at_beginning(self):
        self.assertEqual(find_first_duplicate([2, 1, 2, 3, 4]), 2)

    def test_duplicate_in_middle(self):
        self.assertEqual(find_first_duplicate([1, 2, 2, 3, 4]), 2)

    def test_duplicate_at_end(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 3, 4]), 3)

    def test_duplicates_in_middle_and_end(self):
        self.assertEqual(find_first_duplicate([1, 2, 2, 3, 3, 4]), 2)

    def test_duplicate_with_unique_elements(self):
        self.assertEqual(find_first_duplicate([2, 1, 3, 4, 5, 2]), 2)

    def test_duplicate_with_multiple_occurrences(self):
        self.assertEqual(find_first_duplicate([2, 2, 1, 3, 4, 2]), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_first_duplicate([-1, -2, -2, -3, -4]), -2)

    def test_floating_point_numbers(self):
        self.assertEqual(find_first_duplicate([1.1, 2.2, 2.2, 3.3, 4.4]), 2.2)

    def test_invalid_input_empty_set(self):
        with self.assertRaises(TypeError):
            find_first_duplicate({})

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            find_first_duplicate('abc')
