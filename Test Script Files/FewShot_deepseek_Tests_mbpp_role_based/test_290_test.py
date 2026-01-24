import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_length(['hello', 'world']), (5, 'world'))

    def test_edge_condition(self):
        self.assertEqual(max_length(['a']), (1, 'a'))

    def test_boundary_condition(self):
        self.assertEqual(max_length(['', '']), (0, ''))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_length(123)

        with self.assertRaises(TypeError):
            max_length(['hello', 123])
