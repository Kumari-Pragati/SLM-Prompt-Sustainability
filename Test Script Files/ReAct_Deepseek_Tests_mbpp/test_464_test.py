import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):

    def test_typical_case(self):
        test_dict = {'a': 1, 'b': 1, 'c': 1}
        self.assertTrue(check_value(test_dict, 1))

    def test_edge_case_all_same(self):
        test_dict = {'a': 5, 'b': 5, 'c': 5}
        self.assertTrue(check_value(test_dict, 5))

    def test_edge_case_all_different(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        self.assertFalse(check_value(test_dict, 1))

    def test_edge_case_empty_dict(self):
        test_dict = {}
        self.assertTrue(check_value(test_dict, None))

    def test_edge_case_single_element(self):
        test_dict = {'a': 1}
        self.assertFalse(check_value(test_dict, 2))

    def test_error_case_non_dict_input(self):
        with self.assertRaises(TypeError):
            check_value("not a dict", 1)

    def test_error_case_non_integer_values(self):
        test_dict = {'a': '1', 'b': '1', 'c': '1'}
        with self.assertRaises(TypeError):
            check_value(test_dict, '1')
