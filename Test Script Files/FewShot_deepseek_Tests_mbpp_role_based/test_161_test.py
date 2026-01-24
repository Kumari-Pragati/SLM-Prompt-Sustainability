import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):
    def test_typical_case(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 4]
        self.assertEqual(remove_elements(list1, list2), [1, 3, 5])

    def test_empty_lists(self):
        list1 = []
        list2 = []
        self.assertEqual(remove_elements(list1, list2), [])

    def test_list2_contains_all_elements(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        self.assertEqual(remove_elements(list1, list2), [])

    def test_duplicate_elements(self):
        list1 = [1, 2, 2, 3, 4]
        list2 = [2]
        self.assertEqual(remove_elements(list1, list2), [1, 3, 4])

    def test_negative_numbers(self):
        list1 = [-1, -2, -3, -4, -5]
        list2 = [-2, -4]
        self.assertEqual(remove_elements(list1, list2), [-1, -3, -5])

    def test_mixed_numbers(self):
        list1 = [1, -2, 3, -4, 5]
        list2 = [-2, 3]
        self.assertEqual(remove_elements(list1, list2), [1, -4, 5])
