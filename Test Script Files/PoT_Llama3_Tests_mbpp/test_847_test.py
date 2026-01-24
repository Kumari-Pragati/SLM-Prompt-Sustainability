import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])
        self.assertEqual(lcopy("hello"), "hello")
        self.assertEqual(lcopy([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])
        self.assertEqual(lcopy(""), "")
        self.assertEqual(lcopy([1]), [1])

    def test_boundary(self):
        self.assertEqual(lcopy([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(lcopy([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(lcopy([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_invalid(self):
        with self.assertRaises(TypeError):
            lcopy(None)
        with self.assertRaises(TypeError):
            lcopy(123)
