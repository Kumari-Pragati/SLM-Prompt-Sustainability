import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(5), 10)
        self.assertEqual(smallest_multiple(7), 14)

    def test_edge_cases(self):
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(1), 1)

    def test_corner_cases(self):
        self.assertEqual(smallest_multiple(0), None)
        self.assertEqual(smallest_multiple(-1), None)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            smallest_multiple('3')
        with self.assertRaises(TypeError):
            smallest_multiple(3.5)
