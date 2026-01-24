import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])

    def test_edge_cases(self):
        self.assertEqual(count_variable('a', 'b', '', 'd'), ['a', 'b', 'd'])
        self.assertEqual(count_variable('a', 'b', 'c', ''), ['a', 'b', 'c'])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_variable(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            count_variable('a', 'b', 'c', [4])

    def test_empty_inputs(self):
        self.assertEqual(count_variable('', '', '', ''), [])

    def test_single_input(self):
        self.assertEqual(count_variable('a', '', '', ''), ['a'])

    def test_multiple_inputs(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])
