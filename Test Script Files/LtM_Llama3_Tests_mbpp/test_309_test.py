import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(maximum(1, 2), 2)
        self.assertEqual(maximum(5, 5), 5)
        self.assertEqual(maximum(10, 5), 10)

    def test_edge(self):
        self.assertEqual(maximum(0, 0), 0)
        self.assertEqual(maximum(-1, -2), -1)
        self.assertEqual(maximum(10, 10), 10)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            maximum("a", 2)
        with self.assertRaises(TypeError):
            maximum(2, "b")
