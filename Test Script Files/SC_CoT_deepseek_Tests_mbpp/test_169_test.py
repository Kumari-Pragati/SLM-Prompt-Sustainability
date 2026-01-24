import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(5), 10)

    def test_edge_cases(self):
        self.assertEqual(get_pell(0), 0)
        self.assertEqual(get_pell(3), 4)

    def test_corner_cases(self):
        self.assertEqual(get_pell(10), 34)
        self.assertEqual(get_pell(15), 610)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_pell('a')
        with self.assertRaises(ValueError):
            get_pell(-1)
