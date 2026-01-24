import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(check_alphanumeric('abc123'), 'Accept')

    def test_edge_condition(self):
        self.assertEqual(check_alphanumeric(''), 'Discard')

    def test_boundary_condition(self):
        self.assertEqual(check_alphanumeric('a'), 'Accept')
        self.assertEqual(check_alphanumeric('1'), 'Accept')
        self.assertEqual(check_alphanumeric('A'), 'Accept')
        self.assertEqual(check_alphanumeric(' '), 'Discard')
        self.assertEqual(check_alphanumeric('!'), 'Discard')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_alphanumeric(123)
