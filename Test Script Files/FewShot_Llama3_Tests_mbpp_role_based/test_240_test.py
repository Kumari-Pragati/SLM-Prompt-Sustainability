import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):
    def test_replace_last_element(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [10, 20, 30, 40, 50]
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3, 4, 50])

    def test_replace_last_element_with_empty_list(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = []
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3, 4, 5])

    def test_replace_last_element_with_list_of_same_length(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [6, 7, 8, 9, 10]
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3, 4, 10])

    def test_replace_last_element_with_list_of_shorter_length(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [6, 7, 8]
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3, 4, 8])

    def test_replace_last_element_with_list_of_longer_length(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [6, 7, 8, 9, 10, 11, 12]
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3, 4, 12])
