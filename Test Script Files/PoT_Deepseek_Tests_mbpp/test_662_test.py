import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sorted_dict({'a': [3, 1, 2]}), {'a': [1, 2, 3]})

    def test_empty_dict(self):
        self.assertEqual(sorted_dict({}), {})

    def test_single_key_dict(self):
        self.assertEqual(sorted_dict({'a': [3, 1, 2]}), {'a': [1, 2, 3]})

    def test_duplicate_values(self):
        self.assertEqual(sorted_dict({'a': [3, 1, 2, 2]}), {'a': [1, 2, 2, 3]})

    def test_negative_values(self):
        self.assertEqual(sorted_dict({'a': [-3, -1, -2]}), {'a': [-3, -2, -1]})

    def test_mixed_values(self):
        self.assertEqual(sorted_dict({'a': [3, -1, 2]}), {'a': [-1, 2, 3]})

    def test_empty_list(self):
        self.assertEqual(sorted_dict({'a': []}), {'a': []})
