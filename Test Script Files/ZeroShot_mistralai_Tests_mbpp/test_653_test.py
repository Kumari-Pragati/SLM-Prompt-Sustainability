import unittest
from mbpp_653_code import defaultdict

def grouping_dictionary(l):
    d = defaultdict(list)
    for k, v in l:
        d[k].append(v)
    return d

class TestGroupingDictionary(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(grouping_dictionary([]), {})

    def test_single_element(self):
        self.assertDictEqual(grouping_dictionary([('a', 1)]), {'a': [1]})

    def test_multiple_elements(self):
        self.assertDictEqual(grouping_dictionary([('a', 1), ('a', 2), ('b', 3)]), {'a': [1, 2], 'b': [3]})

    def test_duplicate_keys(self):
        self.assertDictEqual(grouping_dictionary([('a', 1), ('a', 2), ('a', 3), ('b', 4)]), {'a': [1, 2, 3], 'b': [4]})
