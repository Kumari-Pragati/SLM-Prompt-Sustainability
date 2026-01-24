import unittest
from mbpp_391_code import convert_list_dictionary  # replace 'your_module_name' with the actual name of the module containing the function

class TestConvertListDictionary(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(convert_list_dictionary([], [], []), [])

    def test_single_element_lists(self):
        self.assertDictEqual(convert_list_dictionary([1], ['a'], [2]), [{1: {'a': 2}}])
        self.assertDictEqual(convert_list_dictionary(['a'], [1], [2]), [{'a': {1: 2}}])

    def test_multiple_elements_lists(self):
        self.assertDictEqual(convert_list_dictionary([1, 2], ['a', 'b'], [3, 4]),
                             [{1: {'a': 3}, 2: {'b': 4}}])
        self.assertDictEqual(convert_list_dictionary([1, 2], ['b', 'a'], [4, 3]),
                             [{1: {'b': 4}, 2: {'a': 3}}])
