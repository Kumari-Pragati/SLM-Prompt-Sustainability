import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6]), ('c', [7, 8, 9])]
        expected_output = [('a', 3), ('b', 6), ('c', 9)]
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_edge_case(self):
        test_list = [('a', [])]
        expected_output = [('a', None)]
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_boundary_case(self):
        test_list = [('a', [1]), ('b', [2])]
        expected_output = [('a', 1), ('b', 2)]
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_invalid_input(self):
        test_list = 'invalid_input'
        with self.assertRaises(TypeError):
            maximum_value(test_list)
