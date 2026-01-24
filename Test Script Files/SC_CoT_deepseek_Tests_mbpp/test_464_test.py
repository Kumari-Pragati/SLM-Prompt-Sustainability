import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 1}, 1))

    def test_edge_case(self):
        self.assertTrue(check_value({'a': 0, 'b': 0, 'c': 0}, 0))

    def test_boundary_case(self):
        self.assertFalse(check_value({'a': 1, 'b': 2, 'c': 3}, 2))

    def test_special_case(self):
        self.assertFalse(check_value({'a': 1, 'b': 2, 'c': 3}, 3))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_value(123, 1)
