import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):

    def test_replace_list(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3, 4, 5, 6])
        self.assertEqual(replace_list, [1, 2, 3, 4, 5, 6])

    def test_replace_list_empty_list(self):
        list1 = []
        list2 = [4, 5, 6]
        replace_list(list1, list2)
        self.assertEqual(list1, [4, 5, 6])
        self.assertEqual(replace_list, [4, 5, 6])

    def test_replace_list_empty_list2(self):
        list1 = [1, 2, 3]
        list2 = []
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3])
        self.assertEqual(replace_list, [1, 2, 3])

    def test_replace_list_same_list(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        replace_list(list1, list2)
        self.assertEqual(list1, [1, 2, 3])
        self.assertEqual(replace_list, [1, 2, 3])
