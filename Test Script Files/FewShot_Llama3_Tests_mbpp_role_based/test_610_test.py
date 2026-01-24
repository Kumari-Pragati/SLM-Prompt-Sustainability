import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):
    def test_remove_kth_element_from_list(self):
        list1 = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4]
        self.assertEqual(remove_kth_element(list1, 3), expected_result)

    def test_remove_kth_element_from_empty_list(self):
        list1 = []
        expected_result = []
        self.assertEqual(remove_kth_element(list1, 1), expected_result)

    def test_remove_kth_element_from_list_with_k_as_zero(self):
        list1 = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4]
        self.assertEqual(remove_kth_element(list1, 0), expected_result)

    def test_remove_kth_element_from_list_with_k_as_greater_than_length(self):
        list1 = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(remove_kth_element(list1, 6), expected_result)
