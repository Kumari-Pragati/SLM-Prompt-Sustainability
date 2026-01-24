import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurrences(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [['a', 'b', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b']]
        expected_output = {'('a', 'b', 'c')': 1}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_edge_case(self):
        test_list = []
        expected_output = {}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_boundary_case(self):
        test_list = [['a']]
        expected_output = {'('a')': 1}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_invalid_input(self):
        test_list = ['a', 'b', 'c']
        with self.assertRaises(TypeError):
            check_occurences(test_list)
