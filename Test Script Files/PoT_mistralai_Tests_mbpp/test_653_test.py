import unittest
from mbpp_653_code import defaultdict
from six.moves import range

class TestGroupingDictionary(unittest.TestCase):

    def test_typical_case(self):
        self.assertDictEqual(grouping_Dictionary([('a', 1), ('a', 2), ('b', 3), ('a', 4)]),
                             {'a': [1, 2, 4], 'b': [3]})

    def test_empty_list(self):
        self.assertDictEqual(grouping_Dictionary([]), {})

    def test_single_key_single_value(self):
        self.assertDictEqual(grouping_Dictionary([('a', 1)]), {'a': [1]})

    def test_single_key_multiple_values(self):
        self.assertDictEqual(grouping_Dictionary([('a', 1), ('a', 2)]), {'a': [1, 2]})

    def test_multiple_keys_single_value(self):
        self.assertDictEqual(grouping_Dictionary([('a', 1), ('b', 1)]), {'a': [1], 'b': [1]})

    def test_multiple_keys_multiple_values(self):
        self.assertDictEqual(grouping_Dictionary([('a', 1), ('a', 2), ('b', 3), ('a', 4), ('b', 5)]),
                             {'a': [1, 2, 4], 'b': [3, 5]})

    def test_key_with_spaces(self):
        self.assertDictEqual(grouping_Dictionary([('foo bar', 1), ('foo bar', 2)]),
                             {'foo bar': [1, 2]})

    def test_key_with_special_characters(self):
        self.assertDictEqual(grouping_Dictionary([('key#123', 1), ('key#123', 2)]),
                             {'key#123': [1, 2]})

    def test_key_with_special_characters_and_spaces(self):
        self.assertDictEqual(grouping_Dictionary([('key#123 foo', 1), ('key#123 foo', 2)]),
                             {'key#123 foo': [1, 2]})
