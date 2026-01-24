import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_literals('hello world', ['world']), 'Matched!')

    def test_edge_case(self):
        self.assertEqual(check_literals('hello world', ['hello', 'world']), 'Matched!')

    def test_corner_case(self):
        self.assertEqual(check_literals('hello world', ['hello', 'world', 'python']), 'Matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_literals(123, ['world'])
