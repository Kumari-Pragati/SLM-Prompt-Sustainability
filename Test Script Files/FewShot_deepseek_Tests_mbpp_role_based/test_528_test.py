import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_length(['abc', 'defgh', 'ijklm']), (3, 'abc'))

    def test_edge_condition(self):
        self.assertEqual(min_length(['']), (0, ''))

    def test_boundary_condition(self):
        self.assertEqual(min_length(['a', 'ab']), (1, 'a'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_length(123)

        with self.assertRaises(TypeError):
            min_length(['abc', 123])
