import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 4]
        expected_output = [1, 3, 5]
        self.assertEqual(remove_elements(list1, list2), expected_output)

    def test_empty_lists(self):
        list1 = []
        list2 = []
        expected_output = []
        self.assertEqual(remove_elements(list1, list2), expected_output)

    def test_list2_contains_all_elements(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        expected_output = []
        self.assertEqual(remove_elements(list1, list2), expected_output)

    def test_duplicate_elements(self):
        list1 = [1, 2, 2, 3, 4, 4, 5]
        list2 = [2, 4]
        expected_output = [1, 3, 5]
        self.assertEqual(remove_elements(list1, list2), expected_output)

    def test_non_integer_elements(self):
        list1 = [1, 'two', 3, 4, 5]
        list2 = ['two', 4]
        expected_output = [1, 3, 5]
        self.assertEqual(remove_elements(list1, list2), expected_output)

    def test_none_input(self):
        list1 = None
        list2 = [1, 2, 3]
        with self.assertRaises(TypeError):
            remove_elements(list1, list2)

    def test_empty_list2(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = []
        expected_output = list1
        self.assertEqual(remove_elements(list1, list2), expected_output)
