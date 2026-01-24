import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])

    def test_edge_case_empty(self):
        self.assertEqual(count_variable('', '', '', ''), [])

    def test_edge_case_single(self):
        self.assertEqual(count_variable('a', '', '', ''), ['a'])

    def test_edge_case_multiple(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])

    def test_edge_case_duplicates(self):
        self.assertEqual(count_variable('a', 'a', 'c', 'd'), ['a', 'a', 'c', 'd'])

    def test_error_case_non_string(self):
        with self.assertRaises(TypeError):
            count_variable(1, 'b', 'c', 'd')

    def test_error_case_non_string_multiple(self):
        with self.assertRaises(TypeError):
            count_variable(1, 2, 'c', 'd')
