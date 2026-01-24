import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):
    def test_typical_use_case(self):
        result = count_variable('a', 'b', 'c', 'd')
        self.assertEqual(result, ['a', 'b', 'c', 'd'])

    def test_empty_input(self):
        result = count_variable('', '', '', '')
        self.assertEqual(result, [])

    def test_single_input(self):
        result = count_variable('a', '', '', '')
        self.assertEqual(result, ['a'])

    def test_multiple_inputs(self):
        result = count_variable('a', 'b', 'c', 'd')
        self.assertEqual(result, ['a', 'b', 'c', 'd'])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            count_variable(1, 2, 3, 4)
