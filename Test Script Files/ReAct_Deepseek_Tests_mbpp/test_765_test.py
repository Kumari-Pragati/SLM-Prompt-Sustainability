import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(is_polite(1), 3)
        self.assertEqual(is_polite(10), 12)
        self.assertEqual(is_polite(100), 103)

    def test_edge_cases(self):
        self.assertEqual(is_polite(0), 2)
        self.assertEqual(is_polite(-1), 1)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            is_polite('a')
