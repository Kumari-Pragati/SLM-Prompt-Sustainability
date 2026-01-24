import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_element_in_list([], 'x'), 0)

    def test_single_element_list(self):
        self.assertEqual(count_element_in_list(['x'], 'x'), 1)
        self.assertEqual(count_element_in_list(['x'], 'y'), 0)

    def test_multiple_elements_list(self):
        self.assertEqual(count_element_in_list(['x', 'y', 'z'], 'x'), 1)
        self.assertEqual(count_element_in_list(['x', 'y', 'z'], 'y'), 1)
        self.assertEqual(count_element_in_list(['x', 'y', 'z'], 'z'), 1)
        self.assertEqual(count_element_in_list(['x', 'y', 'z'], 'w'), 0)

    def test_nested_list(self):
        self.assertEqual(count_element_in_list([['x', 'y'], ['z', 'x']], 'x'), 2)
        self.assertEqual(count_element_in_list([['x', 'y'], ['z', 'x']], 'y'), 1)
        self.assertEqual(count_element_in_list([['x', 'y'], ['z', 'x']], 'z'), 1)
        self.assertEqual(count_element_in_list([['x', 'y'], ['z', 'x']], 'w'), 0)
