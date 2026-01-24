import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):

    def test_simple_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'d': 5}
        expected = {'a': 1, 'b': 3, 'c': 4, 'd': 5}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_empty_dicts(self):
        self.assertEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_one_empty_dict(self):
        dict1 = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries_three({}, dict1, {}), dict1)

    def test_duplicate_keys(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'b': 5}
        expected = {'a': 1, 'b': 5, 'c': 4}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_large_dicts(self):
        dict1 = {str(i): i for i in range(1000)}
        dict2 = {str(i): i*2 for i in range(1000)}
        dict3 = {str(i): i*3 for i in range(1000)}
        merged_dict = merge_dictionaries_three(dict1, dict2, dict3)
        for i in range(1000):
            self.assertEqual(merged_dict[str(i)], i*3)
