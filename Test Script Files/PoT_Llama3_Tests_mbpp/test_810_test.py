import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])

    def test_edge_case_empty(self):
        self.assertEqual(count_variable('', '', '', ''), [])

    def test_edge_case_single(self):
        self.assertEqual(count_variable('a', '', '', ''), ['a'])

    def test_edge_case_all_empty(self):
        self.assertEqual(count_variable('', '', '', ''), [])

    def test_edge_case_all_same(self):
        self.assertEqual(count_variable('a', 'a', 'a', 'a'), ['a', 'a', 'a', 'a'])

    def test_edge_case_all_diff(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            count_variable(1, 2, 3, 4)
