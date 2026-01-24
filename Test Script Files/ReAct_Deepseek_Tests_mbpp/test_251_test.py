import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_insert_element_typical_case(self):
        input_list = [1, 2, 3]
        element = 4
        expected_output = [4, 1, 4, 2, 4, 3]
        self.assertEqual(insert_element(input_list, element), expected_output)

    def test_insert_element_empty_list(self):
        input_list = []
        element = 1
        expected_output = [1]
        self.assertEqual(insert_element(input_list, element), expected_output)

    def test_insert_element_single_element_list(self):
        input_list = [1]
        element = 2
        expected_output = [2, 1]
        self.assertEqual(insert_element(input_list, element), expected_output)

    def test_insert_element_duplicate_elements(self):
        input_list = [1, 1]
        element = 2
        expected_output = [2, 1, 2, 1]
        self.assertEqual(insert_element(input_list, element), expected_output)

    def test_insert_element_large_list(self):
        input_list = list(range(1, 101))
        element = 0
        expected_output = [0] + input_list
        self.assertEqual(insert_element(input_list, element), expected_output)
