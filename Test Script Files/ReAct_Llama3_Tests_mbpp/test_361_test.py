import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_empty([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_empty([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_empty_string(self):
        self.assertEqual(remove_empty(["", 1, 2, 3]), [1, 2, 3])

    def test_list_with_empty_string_and_numbers(self):
        self.assertEqual(remove_empty(["", 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_empty_string_and_numbers_and_empty_list(self):
        self.assertEqual(remove_empty(["", 1, 2, 3, [], 4, 5]), [1, 2, 3, 4, 5])
