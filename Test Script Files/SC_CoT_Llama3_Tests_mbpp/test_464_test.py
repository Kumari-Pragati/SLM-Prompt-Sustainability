import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):
    def test_typical_input(self):
        dict1 = {'a': 1, 'b': 1, 'c': 1}
        self.assertTrue(check_value(dict1, 1))

    def test_edge_case(self):
        dict2 = {'a': 1, 'b': 2, 'c': 1}
        self.assertFalse(check_value(dict2, 1))

    def test_edge_case2(self):
        dict3 = {'a': 1, 'b': 1, 'c': 2}
        self.assertFalse(check_value(dict3, 1))

    def test_edge_case3(self):
        dict4 = {'a': 1, 'b': 1, 'c': 1, 'd': 2}
        self.assertFalse(check_value(dict4, 1))

    def test_special_case(self):
        dict5 = {'a': '1', 'b': '1', 'c': '1'}
        self.assertFalse(check_value(dict5, 1))

    def test_invalid_input(self):
        dict6 = {'a': 1, 'b': 1, 'c': 'dict'}
        with self.assertRaises(TypeError):
            check_value(dict6, 1)

    def test_empty_dict(self):
        dict7 = {}
        with self.assertRaises(TypeError):
            check_value(dict7, 1)

    def test_non_dict_input(self):
        dict8 = [1, 2, 3]
        with self.assertRaises(TypeError):
            check_value(dict8, 1)
