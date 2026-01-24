import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_typical_input(self):
        list1 = [1, 2, 3, 4, 5]
        element = 3
        self.assertTrue(check_element(list1, element))

    def test_edge_case_empty_list(self):
        list2 = []
        element = 3
        self.assertFalse(check_element(list2, element))

    def test_edge_case_single_element_list(self):
        list3 = [5]
        element = 5
        self.assertTrue(check_element(list3, element))

    def test_edge_case_element_not_in_list(self):
        list4 = [1, 2, 3, 4, 5]
        element = 6
        self.assertFalse(check_element(list4, element))

    def test_edge_case_element_in_list(self):
        list5 = [1, 2, 3, 4, 5]
        element = 3
        self.assertTrue(check_element(list5, element))

    def test_edge_case_list_with_duplicates(self):
        list6 = [1, 2, 2, 3, 3, 3]
        element = 3
        self.assertTrue(check_element(list6, element))

    def test_edge_case_list_with_duplicates_and_non_duplicates(self):
        list7 = [1, 2, 2, 3, 3, 3, 4, 5]
        element = 3
        self.assertTrue(check_element(list7, element))

    def test_invalid_input_non_list(self):
        list8 = "hello"
        element = 3
        with self.assertRaises(TypeError):
            check_element(list8, element)

    def test_invalid_input_non_integer_element(self):
        list9 = [1, 2, 3, 4, 5]
        element = "hello"
        with self.assertRaises(TypeError):
            check_element(list9, element)
