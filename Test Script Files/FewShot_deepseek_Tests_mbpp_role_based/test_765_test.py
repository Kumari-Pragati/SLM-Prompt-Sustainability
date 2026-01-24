import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(is_polite(10), 12)

    def test_boundary_conditions(self):
        self.assertEqual(is_polite(0), 1)
        self.assertEqual(is_polite(1), 2)

    def test_edge_conditions(self):
        self.assertEqual(is_polite(-1), 0)
        self.assertEqual(is_polite(2), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_polite('a')
        with self.assertRaises(TypeError):
            is_polite(None)
