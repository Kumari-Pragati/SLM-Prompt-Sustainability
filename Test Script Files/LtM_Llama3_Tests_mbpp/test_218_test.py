import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(min_Operations(2, 2), 1)
        self.assertEqual(min_Operations(5, 5), 4)
        self.assertEqual(min_Operations(10, 10), 9)

    def test_edge(self):
        self.assertEqual(min_Operations(0, 0), 0)
        self.assertEqual(min_Operations(1, 1), 0)
        self.assertEqual(min_Operations(2, 0), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            min_Operations('a', 2)
        with self.assertRaises(TypeError):
            min_Operations(2, 'b')

    def test_complex(self):
        self.assertEqual(min_Operations(3, 6), 2)
        self.assertEqual(min_Operations(4, 8), 3)
        self.assertEqual(min_Operations(5, 10), 4)
