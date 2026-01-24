import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):
    def test_simple_replace(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3, 4, 5, 6])

    def test_replace_empty_list(self):
        list1 = []
        list2 = [4, 5, 6]
        replace_list(list1, list2)
        self.assertEqual(list1, [4, 5, 6])

    def test_replace_with_empty_list(self):
        list1 = [1, 2, 3]
        list2 = []
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3])

    def test_replace_with_same_list(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3])

    def test_replace_with_longer_list(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6, 7, 8, 9]
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_replace_with_shorter_list(self):
        list1 = [1, 2, 3, 4, 5, 6]
        list2 = [4, 5, 6]
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3, 4, 5, 6])
