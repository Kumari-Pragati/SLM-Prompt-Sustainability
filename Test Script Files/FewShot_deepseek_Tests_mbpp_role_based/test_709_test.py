import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('a', 1), ('b', 1), ('c', 2), ('d', 2)]
        expected_output = "{'1': 2, '2': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_edge_case(self):
        test_list = []
        expected_output = "{}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_boundary_case(self):
        test_list = [('a', 1)] * 10000
        expected_output = "{'1': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [('a', 1), ('b', 'two')]  # invalid input
        with self.assertRaises(TypeError):
            get_unique(test_list)
