import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):
    def test_typical_case(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [4, 5, 6])

    def test_empty_list2(self):
        list1 = [1, 2, 3]
        list2 = []
        result = replace_list(list1, list2)
        self.assertEqual(result, [])

    def test_single_element_list2(self):
        list1 = [1, 2, 3]
        list2 = [4]
        result = replace_list(list1, list2)
        self.assertEqual(result, [4])

    def test_empty_list1(self):
        list1 = []
        list2 = [4, 5, 6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [4, 5, 6])

    def test_same_length_lists(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [4, 5, 6])

    def test_list1_with_single_element(self):
        list1 = [1]
        list2 = [4, 5, 6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [4, 5, 6])

    def test_negative_numbers(self):
        list1 = [-1, -2, -3]
        list2 = [-4, -5, -6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [-4, -5, -6])

    def test_large_numbers(self):
        list1 = [1000, 2000, 3000]
        list2 = [4000, 5000, 6000]
        result = replace_list(list1, list2)
        self.assertEqual(result, [4000, 5000, 6000])

    def test_invalid_input(self):
        list1 = [1, 2, 3]
        list2 = "not a list"
        with self.assertRaises(TypeError):
            replace_list(list1, list2)
