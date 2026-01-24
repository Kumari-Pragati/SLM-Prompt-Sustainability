import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(repeat_tuples((1, 2), 3), ((1, 2),) * 3)

    def test_edge(self):
        self.assertEqual(repeat_tuples((), 5), () * 5)

    def test_boundary(self):
        self.assertEqual(repeat_tuples((1, 2), 0), ())

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            repeat_tuples(None, 1)

    def test_edge_invalid_input(self):
        with self.assertRaises(TypeError):
            repeat_tuples(None, 0)
