import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(sorted_dict({}), {})

    def test_single_key_dict(self):
        self.assertEqual(sorted_dict({'a': [1, 2, 3]}), {'a': [1, 2, 3]})

    def test_multiple_key_dict(self):
        self.assertEqual(sorted_dict({'a': [1, 2, 3], 'b': [4, 5, 6]}), {'a': [1, 2, 3], 'b': [4, 5, 6]})

    def test_dict_with_empty_list(self):
        self.assertEqual(sorted_dict({'a': []}), {'a': []})

    def test_dict_with_single_element_list(self):
        self.assertEqual(sorted_dict({'a': [1]}), {'a': [1]})

    def test_dict_with_multiple_element_list(self):
        self.assertEqual(sorted_dict({'a': [1, 2, 3, 4, 5]}), {'a': [1, 2, 3, 4, 5]})
