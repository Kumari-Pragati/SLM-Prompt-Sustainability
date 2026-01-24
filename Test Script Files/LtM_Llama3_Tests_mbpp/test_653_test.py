import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(grouping_dictionary([]), {})

    def test_single_element_input(self):
        self.assertEqual(grouping_dictionary([(1, 2)]), {1: [2]})

    def test_multiple_elements_input(self):
        self.assertEqual(grouping_dictionary([(1, 2), (1, 3), (2, 4)]), {1: [2, 3], 2: [4]})

    def test_empty_key_input(self):
        self.assertEqual(grouping_dictionary([(None, 2), (None, 3)]), {None: [2, 3]})

    def test_empty_value_input(self):
        self.assertEqual(grouping_dictionary([(1, [])]), {1: [[]]})

    def test_non_list_value_input(self):
        self.assertEqual(grouping_dictionary([(1, 2)]), {1: [2]})

    def test_non_list_key_input(self):
        self.assertEqual(grouping_dictionary([(1, 2), (1, 3), (2, 4)]), {1: [2, 3], 2: [4]})
