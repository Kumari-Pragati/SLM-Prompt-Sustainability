import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):

    def test_simple_input(self):
        self.assertTrue(check_value({'a': 1, 'b': 1}, 1))
        self.assertFalse(check_value({'a': 1, 'b': 2}, 1))

    def test_empty_input(self):
        self.assertTrue(check_value({}, 1))
        self.assertTrue(check_value({}, 0))

    def test_edge_values(self):
        self.assertTrue(check_value({'a': -1, 'b': -1}, -1))
        self.assertFalse(check_value({'a': -1, 'b': 0}, -1))

    def test_complex_input(self):
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 1}, 1))
        self.assertFalse(check_value({'a': 1, 'b': 2, 'c': 3}, 1))
