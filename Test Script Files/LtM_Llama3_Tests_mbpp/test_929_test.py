import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_tuplex((1, 2, 3), 1), 1)
        self.assertEqual(count_tuplex((1, 2, 3), 2), 1)
        self.assertEqual(count_tuplex((1, 2, 3), 3), 1)
        self.assertEqual(count_tuplex((1, 2, 3), 4), 0)

    def test_empty(self):
        self.assertEqual(count_tuplex([], 1), 0)
        self.assertEqual(count_tuplex([], 2), 0)
        self.assertEqual(count_tuplex([], 3), 0)

    def test_single(self):
        self.assertEqual(count_tuplex((1,), 1), 1)
        self.assertEqual(count_tuplex((1,), 2), 0)
        self.assertEqual(count_tuplex((1,), 3), 0)

    def test_edge(self):
        self.assertEqual(count_tuplex((1, 1, 1), 1), 3)
        self.assertEqual(count_tuplex((1, 2, 3), 1), 1)
        self.assertEqual(count_tuplex((1, 2, 3), 3), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            count_tuplex(None, 1)
        with self.assertRaises(TypeError):
            count_tuplex("hello", 1)
