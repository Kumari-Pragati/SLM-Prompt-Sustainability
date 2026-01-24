import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(first_odd([2, 4, 6, 8, 10]), -1)
        self.assertEqual(first_odd([2, 4, 7, 8, 10]), 7)

    def test_edge_conditions(self):
        self.assertEqual(first_odd([]), -1)
        self.assertEqual(first_odd([2, 4, 6, 8]), -1)
        self.assertEqual(first_odd([1]), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_odd("1, 2, 3")
        with self.assertRaises(TypeError):
            first_odd(123)
        with self.assertRaises(TypeError):
            first_odd(None)
