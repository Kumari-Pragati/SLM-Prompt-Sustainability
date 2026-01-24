import unittest
from mbpp_668_code import replace

class TestReplace(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace('hello', 'l'), 'heo')

    def test_edge_condition(self):
        self.assertEqual(replace('', 'a'), '')

    def test_boundary_condition(self):
        self.assertEqual(replace('a'*10000, 'a'), '')

    def test_single_char(self):
        self.assertEqual(replace('hello', 'h'), 'ello')

    def test_no_match(self):
        self.assertEqual(replace('hello', 'z'), 'hello')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace(123, 'a')
