import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):
    def test_typical_use_case(self):
        test_dict = {'a': 1, 'b': 1, 'c': 1}
        self.assertTrue(check_value(test_dict, 1))

    def test_edge_condition(self):
        test_dict = {'a': 0, 'b': 0, 'c': 0}
        self.assertTrue(check_value(test_dict, 0))

    def test_boundary_condition(self):
        test_dict = {'a': 1000, 'b': 1000, 'c': 1000}
        self.assertTrue(check_value(test_dict, 1000))

    def test_different_values(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        self.assertFalse(check_value(test_dict, 2))

    def test_empty_dictionary(self):
        test_dict = {}
        self.assertTrue(check_value(test_dict, None))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_value(123, 1)
