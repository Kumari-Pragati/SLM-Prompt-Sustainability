import unittest
from mbpp_698_code import str, range
from six.moves import map

from sort_dict_item import sort_dict_item

class TestSortDictItem(unittest.TestCase):

    def test_normal_inputs(self):
        test_dict_1 = {'a1': (1, 'apple'), 'a2': (2, 'banana'), 'a3': (3, 'cherry')}
        self.assertDictEqual(sort_dict_item(test_dict_1), {'a3': ('cherry', 3), 'a1': ('apple', 1), 'a2': ('banana', 2)})

        test_dict_2 = {'b1': (10, 'orange'), 'b2': (20, 'grape'), 'b3': (30, 'lemon')}
        self.assertDictEqual(sort_dict_item(test_dict_2), {'b3': ('lemon', 30), 'b1': ('orange', 10), 'b2': ('grape', 20)})

    def test_edge_and_boundary_conditions(self):
        test_dict_3 = {'c1': (0, 'mango'), 'c2': (0, 'pear'), 'c3': (1, 'kiwi')}
        self.assertDictEqual(sort_dict_item(test_dict_3), {'c3': ('kiwi', 1), 'c1': ('mango', 0), 'c2': ('pear', 0)})

        test_dict_4 = {'d1': (100, 'pineapple'), 'd2': (100, 'watermelon'), 'd3': (101, 'guava')}
        self.assertDictEqual(sort_dict_item(test_dict_4), {'d3': ('guava', 101), 'd1': ('pineapple', 100), 'd2': ('watermelon', 100)})

        test_dict_5 = {'e1': (0, 'avocado'), 'e2': (0, 'tomato'), 'e3': (0, 'potato')}
        self.assertDictEqual(sort_dict_item(test_dict_5), {'e1': ('avocado', 0), 'e2': ('tomato', 0), 'e3': ('potato', 0)})

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sort_dict_item(123)

        with self.assertRaises(TypeError):
            sort_dict_item(['a', 'b', 'c'])
