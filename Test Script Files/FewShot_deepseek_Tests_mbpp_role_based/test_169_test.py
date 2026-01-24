import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):
    def test_typical_use_cases(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(5), 22)

    def test_edge_conditions(self):
        self.assertEqual(get_pell(0), 0)
        self.assertEqual(get_pell(-1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(get_pell(3), 5)
        self.assertEqual(get_pell(4), 12)
        self.assertEqual(get_pell(10), 34)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_pell('a')
        with self.assertRaises(TypeError):
            get_pell(None)
