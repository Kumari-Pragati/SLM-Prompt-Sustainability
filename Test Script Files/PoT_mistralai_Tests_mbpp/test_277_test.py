import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):

    def test_typical_case(self):
        self.assertDictEqual(dict_filter({1: 5, 2: 3, 3: 7, 4: 2}, 4), {3: 7, 4: 2})
        self.assertDictEqual(dict_filter({'a': 10, 'b': 15, 'c': 5, 'd': 0}, 10), {'a': 10})
        self.assertDictEqual(dict_filter({1.0: 5.5, 2.0: 3.0, 3.0: 7.0, 4.0: 2.0}, 3.5), {2.0: 3.0, 3.0: 7.0})

    def test_edge_case(self):
        self.assertDictEqual(dict_filter({1: 0, 2: 3, 3: 7, 4: 2}, 1), {})
        self.assertDictEqual(dict_filter({1: -1, 2: 3, 3: 7, 4: 2}, 0), {2: 3, 3: 7, 4: 2})
        self.assertDictEqual(dict_filter({1: 1.0000000000000001, 2: 3, 3: 7, 4: 2}, 1), {2: 3, 3: 7, 4: 2})

    def test_corner_case(self):
        self.assertDictEqual(dict_filter({None: 5, 2: 3, 3: 7, 4: 2}, 3), {2: 3, 3: 7, 4: 2})
        self.assertDictEqual(dict_filter({1: 5, 2: 3, 3: 7, 4: 2, 5: 5}, 6), {})
