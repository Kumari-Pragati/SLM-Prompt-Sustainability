import unittest
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):

    def test_typical_case(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 5, 'c': 4}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_edge_case_empty_dict(self):
        d1 = {}
        d2 = {'b': 3, 'c': 4}
        expected = {'b': 3, 'c': 4}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_boundary_case_same_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 3, 'b': 4}
        expected = {'a': 4, 'b': 6}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_invalid_input(self):
        d1 = {'a': 1, 'b': 2}
        d2 = 'not a dictionary'
        with self.assertRaises(TypeError):
            add_dict(d1, d2)
