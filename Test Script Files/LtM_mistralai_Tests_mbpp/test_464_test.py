import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(check_value({'a': 1, 'b': 1}, 1))
        self.assertFalse(check_value({'a': 1, 'b': 2}, 1))

    def test_edge_cases(self):
        self.assertTrue(check_value({}, None))
        self.assertFalse(check_value({'a': 1}, None))
        self.assertFalse(check_value({'a': 1}, 0))
        self.assertFalse(check_value({'a': 1}, float('inf')))
        self.assertFalse(check_value({'a': 1}, -1))

    def test_complex_cases(self):
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 1}, 1))
        self.assertFalse(check_value({'a': 1, 'b': 1, 'c': 2}, 1))
        self.assertFalse(check_value({'a': 1, 'b': 1, 'c': None}, 1))
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 0}, False))
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': float('inf')}, False))
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': -1}, False))
