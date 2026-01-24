import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):
    def test_remove_elements_from_empty_list(self):
        self.assertEqual(remove_elements([], [1, 2, 3]), [])

    def test_remove_elements_from_non_empty_list(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [2, 4]), [1, 3, 5])

    def test_remove_elements_from_list_with_duplicates(self):
        self.assertEqual(remove_elements([1, 2, 2, 3, 4, 4, 5], [2, 4]), [1, 3, 5])

    def test_remove_elements_from_list_with_duplicates_and_order_matters(self):
        self.assertEqual(remove_elements([1, 2, 2, 3, 4, 4, 5], [2, 4, 2]), [1, 3, 5])

    def test_remove_elements_from_list_with_duplicates_and_order_doesnt_matter(self):
        self.assertEqual(remove_elements([1, 2, 2, 3, 4, 4, 5], [2, 4]), [1, 3, 5])

    def test_remove_elements_from_list_with_duplicates_and_order_doesnt_matter_and_duplicates(self):
        self.assertEqual(remove_elements([1, 2, 2, 3, 4, 4, 5], [2, 4, 2, 4]), [1, 3, 5])
