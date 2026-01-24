import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):
    def test_replace_list(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
        self.assertEqual(list1, [1, 2, 3, 4, 5, 6])

    def test_replace_list_empty(self):
        list1 = []
        list2 = [4, 5, 6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [4, 5, 6])
        self.assertEqual(list1, [4, 5, 6])

    def test_replace_list_single_element(self):
        list1 = [1]
        list2 = [4, 5, 6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [1, 4, 5, 6])
        self.assertEqual(list1, [1, 4, 5, 6])

    def test_replace_list_empty_lists(self):
        list1 = []
        list2 = []
        result = replace_list(list1, list2)
        self.assertEqual(result, [])
        self.assertEqual(list1, [])

    def test_replace_list_invalid_input(self):
        list1 = [1, 2, 3]
        list2 = 'invalid input'
        with self.assertRaises(TypeError):
            replace_list(list1, list2)
