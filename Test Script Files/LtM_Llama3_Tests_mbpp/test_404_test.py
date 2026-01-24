import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(minimum(1, 2), 1)
        self.assertEqual(minimum(3, 3), 3)
        self.assertEqual(minimum(5, 1), 1)

    def test_edge(self):
        self.assertEqual(minimum(0, 1), 0)
        self.assertEqual(minimum(-1, 1), -1)
        self.assertEqual(minimum(1, 0), 0)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            minimum("a", 2)
        with self.assertRaises(TypeError):
            minimum(2, "b")
