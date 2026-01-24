import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)

    def test_edge_cases(self):
        self.assertEqual(catalan_number(-1), 1)
        self.assertEqual(catalan_number(0.5), 1)
        self.assertEqual(catalan_number(1.5), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            catalan_number('a')
        with self.assertRaises(TypeError):
            catalan_number(None)
