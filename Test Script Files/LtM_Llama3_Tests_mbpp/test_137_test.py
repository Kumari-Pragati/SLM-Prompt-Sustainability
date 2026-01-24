import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):
    def test_zero_count_typical(self):
        self.assertEqual(zero_count([0, 1, 2, 0, 3, 4, 0]), 0.4)
        self.assertEqual(zero_count([1, 2, 3, 4, 5]), 0.0)
        self.assertEqual(zero_count([0, 0, 0, 0, 0]), 1.0)

    def test_zero_count_edge(self):
        self.assertEqual(zero_count([]), 0.0)
        self.assertEqual(zero_count([0]), 1.0)
        self.assertEqual(zero_count([1]), 0.0)

    def test_zero_count_invalid(self):
        with self.assertRaises(TypeError):
            zero_count(None)
        with self.assertRaises(TypeError):
            zero_count("hello")
