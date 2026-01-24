import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):

    def test_empty_dict(self):
        self.assertDictEqual(sort_dict_item({}), {})

    def test_single_item_dict(self):
        self.assertDictEqual(sort_dict_item({(1, 2): 'a'}), {('2', '1'): 'a'})

    def test_multiple_items_dict(self):
        self.assertDictEqual(sort_dict_item({((1, 2), 'x'): 1, ((3, 4), 'y'): 2, ((5, 6), 'z'): 3}),
                             {('x', '1, 2'): 1, ('y', '3, 4'): 2, ('z', '5, 6'): 3})

    def test_negative_numbers(self):
        self.assertDictEqual(sort_dict_item({((-1, 2), 'x'): 1, ((3, -4), 'y'): 2, ((5, -6), 'z'): 3}),
                             {('x', '-1, 2'): 1, ('y', '3, -4'): 2, ('z', '5, -6'): 3})

    def test_floats(self):
        self.assertDictEqual(sort_dict_item({((1.1, 2), 'x'): 1, ((3, 4.4), 'y'): 2, ((5, 6.6), 'z'): 3}),
                             {('x', '1.1, 2'): 1, ('y', '3, 4.4'): 2, ('z', '5, 6.6'): 3})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_dict_item([(1, 2), (3, 4)])
