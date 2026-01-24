import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_odd([2, 4, 6, 8, 10]), -1)
        self.assertEqual(first_odd([2, 4, 6, 8, 11]), 11)

    def test_edge_cases(self):
        self.assertEqual(first_odd([]), -1)
        self.assertEqual(first_odd([2]), -1)
        self.assertEqual(first_odd([2, 4, 6, 8, 10, 12]), -1)

    def test_corner_cases(self):
        self.assertEqual(first_odd([1]), 1)
        self.assertEqual(first_odd([2, 3]), 3)
        self.assertEqual(first_odd([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_odd(123)
        with self.assertRaises(TypeError):
            first_odd("123")
        with self.assertRaises(TypeError):
            first_odd(None)
