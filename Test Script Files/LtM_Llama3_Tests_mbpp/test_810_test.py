import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])

    def test_empty_inputs(self):
        self.assertEqual(count_variable('', '', '', ''), [])

    def test_single_input(self):
        self.assertEqual(count_variable('a', '', '', ''), ['a'])

    def test_multiple_inputs(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])

    def test_edge_case(self):
        self.assertEqual(count_variable('a', 'a', 'a', 'a'), ['a', 'a', 'a', 'a'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_variable(1, 2, 3, 4)
