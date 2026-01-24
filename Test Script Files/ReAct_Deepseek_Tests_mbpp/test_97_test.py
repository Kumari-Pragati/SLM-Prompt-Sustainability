import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
        expected_output = {1: 1, 2: 2, 3: 2, 4: 2, 5: 1, 6: 1}
        self.assertEqual(frequency_lists(list1), expected_output)

    def test_empty_list(self):
        list1 = []
        expected_output = {}
        self.assertEqual(frequency_lists(list1), expected_output)

    def test_single_element_list(self):
        list1 = [[1]]
        expected_output = {1: 1}
        self.assertEqual(frequency_lists(list1), expected_output)

    def test_duplicate_elements(self):
        list1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        expected_output = {1: 3, 2: 3, 3: 3}
        self.assertEqual(frequency_lists(list1), expected_output)

    def test_mixed_types(self):
        list1 = [['a', 'b', 'c'], ['b', 'c', 'd'], ['d', 'e', 'f']]
        expected_output = {'a': 1, 'b': 2, 'c': 2, 'd': 2, 'e': 1, 'f': 1}
        self.assertEqual(frequency_lists(list1), expected_output)
