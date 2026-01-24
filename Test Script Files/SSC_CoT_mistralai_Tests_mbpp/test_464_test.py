import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 1}, 1))

    def test_edge_case_single_value(self):
        self.assertTrue(check_value({'a': 1}, 1))
        self.assertFalse(check_value({'a': 1}, 2))

    def test_edge_case_empty_dict(self):
        self.assertFalse(check_value({}, 1))

    def test_edge_case_multiple_values(self):
        self.assertTrue(check_value({'a': 1, 'b': 2, 'c': 3}, 1))
        self.assertFalse(check_value({'a': 1, 'b': 2, 'c': 3}, 4))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_value({'a': 1, 'b': 'two'}, 1)
