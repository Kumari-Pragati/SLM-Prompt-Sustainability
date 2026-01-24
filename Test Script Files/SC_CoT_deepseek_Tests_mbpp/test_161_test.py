import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 4]
        self.assertEqual(remove_elements(list1, list2), [1, 3, 5])

    def test_empty_list2(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = []
        self.assertEqual(remove_elements(list1, list2), list1)

    def test_empty_list1(self):
        list1 = []
        list2 = [2, 4]
        self.assertEqual(remove_elements(list1, list2), [])

    def test_all_elements_in_list2(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        self.assertEqual(remove_elements(list1, list2), [])

    def test_duplicate_elements_in_list2(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 2, 4, 4]
        self.assertEqual(remove_elements(list1, list2), [1, 3, 5])

    def test_duplicate_elements_in_list1(self):
        list1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        list2 = [2, 4]
        self.assertEqual(remove_elements(list1, list2), [1, 1, 3, 3, 5, 5])

    def test_invalid_input(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = 'not a list'
        with self.assertRaises(TypeError):
            remove_elements(list1, list2)
