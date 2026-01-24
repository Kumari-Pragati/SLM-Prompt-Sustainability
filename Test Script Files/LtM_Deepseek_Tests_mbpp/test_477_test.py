import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(is_lower('Hello'), 'hello')
        self.assertEqual(is_lower('WORLD'), 'world')

    def test_edge_conditions(self):
        self.assertEqual(is_lower(''), '')
        self.assertEqual(is_lower('123'), '123')
        self.assertEqual(is_lower('!@#'), '!@#')

    def test_complex_cases(self):
        self.assertEqual(is_lower('hElLo'), 'hello')
        self.assertEqual(is_lower('wOrLd'), 'world')
        self.assertEqual(is_lower('123!@#'), '123!@#')
