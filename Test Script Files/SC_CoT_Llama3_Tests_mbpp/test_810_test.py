import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])

    def test_edge_cases(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])

    def test_edge_case_empty(self):
        self.assertEqual(count_variable('', '', '', ''), [])

    def test_edge_case_single(self):
        self.assertEqual(count_variable('a', '', '', ''), ['a'])
        self.assertEqual(count_variable('', 'b', '', ''), ['b'])
        self.assertEqual(count_variable('', '', 'c', ''), ['c'])
        self.assertEqual(count_variable('', '', '', 'd'), ['d'])

    def test_edge_case_multiple(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_variable(1, 'b', 'c', 'd')
        with self.assertRaises(TypeError):
            count_variable('a', 1, 'c', 'd')
        with self.assertRaises(TypeError):
            count_variable('a', 'b', 1, 'd')
        with self.assertRaises(TypeError):
            count_variable('a', 'b', 'c', 1)
