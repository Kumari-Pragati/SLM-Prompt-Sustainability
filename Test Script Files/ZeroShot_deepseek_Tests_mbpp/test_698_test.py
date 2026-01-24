import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):

    def test_sort_dict_item(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        expected_output = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

        test_dict = {'b': 2, 'a': 1, 'c': 3}
        expected_output = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

        test_dict = {'b': 2, 'a': 1, 'c': 3, 'd': 4}
        expected_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

        test_dict = {'b': 2, 'a': 1, 'c': 3, 'd': 4, 'e': 5}
        expected_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

        test_dict = {'b': 2, 'a': 1, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
        expected_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
        self.assertEqual(sort_dict_item(test_dict), expected_output)
