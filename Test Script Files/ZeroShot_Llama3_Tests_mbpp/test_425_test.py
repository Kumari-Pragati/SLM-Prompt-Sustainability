import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_count_element_in_list(self):
        self.assertEqual(count_element_in_list(['apple', 'banana', 'cherry'], 'apple'), 1)
        self.assertEqual(count_element_in_list(['apple', 'banana', 'cherry'], 'banana'), 1)
        self.assertEqual(count_element_in_list(['apple', 'banana', 'cherry'], 'cherry'), 1)
        self.assertEqual(count_element_in_list(['apple', 'banana', 'cherry'], 'grape'), 0)
        self.assertEqual(count_element_in_list([], 'apple'), 0)
        self.assertEqual(count_element_in_list(['apple'], 'apple'), 1)
        self.assertEqual(count_element_in_list(['apple', 'banana', 'cherry'], 'apple,banana,cherry'), 1)
        self.assertEqual(count_element_in_list(['apple', 'banana', 'cherry'], 'apple,banana'), 2)
        self.assertEqual(count_element_in_list(['apple', 'banana', 'cherry'], 'apple,banana,cherry,orange'), 3)

    def test_count_element_in_list_with_empty_list(self):
        self.assertEqual(count_element_in_list([], 'apple'), 0)

    def test_count_element_in_list_with_single_element(self):
        self.assertEqual(count_element_in_list(['apple'], 'apple'), 1)

    def test_count_element_in_list_with_multiple_elements(self):
        self.assertEqual(count_element_in_list(['apple', 'banana', 'cherry'], 'apple'), 1)
        self.assertEqual(count_element_in_list(['apple', 'banana', 'cherry'], 'banana'), 1)
        self.assertEqual(count_element_in_list(['apple', 'banana', 'cherry'], 'cherry'), 1)
