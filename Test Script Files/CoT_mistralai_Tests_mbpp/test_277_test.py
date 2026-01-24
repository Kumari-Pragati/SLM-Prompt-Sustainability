import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):
    def test_empty_dict(self):
        self.assertDictEqual({}, dict_filter({}, 10))

    def test_no_filter_condition(self):
        self.assertDictEqual({'key1': 5, 'key2': 10}, dict_filter({'key1': 5, 'key2': 10}, 0))

    def test_typical_case(self):
        self.assertDictEqual({'key1': 15, 'key2': 10}, dict_filter({'key1': 15, 'key2': 10}, 10))

    def test_edge_case_zero(self):
        self.assertDictEqual({'key1': 0}, dict_filter({'key1': 0, 'key2': 1}, 1))

    def test_edge_case_negative(self):
        self.assertDictEqual({}, dict_filter({'key1': -5, 'key2': -10}, 0))

    def test_invalid_input_non_dict(self):
        with self.assertRaises(TypeError):
            dict_filter('not_a_dict', 10)
