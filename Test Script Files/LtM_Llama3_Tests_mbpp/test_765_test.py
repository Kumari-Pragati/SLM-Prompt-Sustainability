import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(is_polite(0), 1)
        self.assertEqual(is_polite(1), 2)
        self.assertEqual(is_polite(2), 3)
        self.assertEqual(is_polite(3), 4)

    def test_edge_cases(self):
        self.assertEqual(is_polite(-1), 1)
        self.assertEqual(is_polite(-2), 2)
        self.assertEqual(is_polite(0.5), 1)
        self.assertEqual(is_polite(0.9), 2)

    def test_boundary_cases(self):
        self.assertEqual(is_polite(10), 11)
        self.assertEqual(is_polite(100), 101)
        self.assertEqual(is_polite(1000), 1001)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_polite('a')
        with self.assertRaises(TypeError):
            is_polite(None)
