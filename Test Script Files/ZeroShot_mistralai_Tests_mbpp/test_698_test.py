import unittest
from mbpp_698_code import SortedDict
from six.moves import range

def sort_dict_item(test_dict):
  res = {key: test_dict[key] for key in sorted(test_dict.keys(), key = lambda ele: ele[1] * ele[0])}
  return  (res)

class TestSortDictItem(unittest.TestCase):

    def test_empty_dict(self):
        self.assertDictEqual({}, sort_dict_item({}))

    def test_single_item_dict(self):
        self.assertDictEqual({'a': 1}, sort_dict_item({'a': 1}))

    def test_multiple_items_dict(self):
        test_dict = {'a': (1, 2), 'b': (3, 1), 'c': (1, 3), 'd': (2, 4)}
        expected_dict = {'c': 1, 'a': 2, 'd': 4, 'b': 3}
        self.assertDictEqual(expected_dict, sort_dict_item(test_dict))
