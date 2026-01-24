import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 4]
        expected_result = [1, 3, 5]
        self.assertEqual(remove_elements(list1, list2), expected_result)

    def test_empty_lists(self):
        list1 = []
        list2 = []
        expected_result = []
        self.assertEqual(remove_elements(list1, list2), expected_result)

    def test_list1_empty(self):
        list1 = []
        list2 = [1, 2, 3]
        expected_result = []
        self.assertEqual(remove_elements(list1, list2), expected_result)

    def test_list2_empty(self):
        list1 = [1, 2, 3]
        list2 = []
        expected_result = list1
        self.assertEqual(remove_elements(list1, list2), expected_result)

    def test_duplicates_in_list2(self):
        list1 = [1, 2, 2, 3, 4]
        list2 = [2]
        expected_result = [1, 3, 4]
        self.assertEqual(remove_elements(list1, list2), expected_result)

    def test_duplicates_in_list1(self):
        list1 = [1, 2, 2, 3, 4]
        list2 = [2]
        expected_result = [1, 3, 4]
        self.assertEqual(remove_elements(list1, list2), expected_result)

    def test_all_elements_in_list2(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        expected_result = []
        self.assertEqual(remove_elements(list1, list2), expected_result)
