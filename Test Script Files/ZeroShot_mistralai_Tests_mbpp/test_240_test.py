import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(replace_list([], ['a']), ['a'])

    def test_single_element_list(self):
        self.assertListEqual(replace_list(['a'], ['b']), ['b'])

    def test_multiple_elements_list(self):
        self.assertListEqual(replace_list(['a', 'b', 'c'], ['d', 'e']), ['d', 'e', 'c'])

    def test_same_last_element(self):
        self.assertListEqual(replace_list(['a', 'a'], ['b']), ['b', 'a'])

    def test_different_data_types(self):
        self.assertRaises(TypeError, replace_list, [1, 2, 3], [4, 'a'])
