import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):
    def test_typical_case(self):
        dict_1 = {'a': 1, 'b': 1, 'c': 1}
        self.assertTrue(check_value(dict_1, 1))

    def test_edge_case_single_value(self):
        dict_2 = {'x': 1}
        self.assertTrue(check_value(dict_2, 1))

    def test_edge_case_empty_dict(self):
        self.assertFalse(check_value({}, 1))

    def test_edge_case_multiple_values(self):
        dict_3 = {'a': 1, 'b': 2, 'c': 1}
        self.assertFalse(check_value(dict_3, 1))

    def test_invalid_input_non_dict(self):
        with self.assertRaises(TypeError):
            check_value('str', 1)

    def test_invalid_input_non_number(self):
        with self.assertRaises(TypeError):
            check_value({'a': 'str'}, 1)
