import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(check_alphanumeric('abc123'), 'Accept')
        self.assertEqual(check_alphanumeric('ABC123'), 'Accept')
        self.assertEqual(check_alphanumeric('123'), 'Accept')
        self.assertEqual(check_alphanumeric('abc'), 'Accept')

    def test_edge_cases(self):
        self.assertEqual(check_alphanumeric(''), 'Discard')
        self.assertEqual(check_alphanumeric(' '), 'Discard')
        self.assertEqual(check_alphanumeric('!@#'), 'Discard')
        self.assertEqual(check_alphanumeric('$%^'), 'Discard')

    def test_special_cases(self):
        self.assertEqual(check_alphanumeric('abc123$'), 'Discard')
        self.assertEqual(check_alphanumeric('ABC123$'), 'Discard')
        self.assertEqual(check_alphanumeric('123$'), 'Discard')
        self.assertEqual(check_alphanumeric('abc$'), 'Discard')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_alphanumeric(123)
        with self.assertRaises(TypeError):
            check_alphanumeric(None)
        with self.assertRaises(TypeError):
            check_alphanumeric(True)
        with self.assertRaises(TypeError):
            check_alphanumeric([1, 2, 3])
