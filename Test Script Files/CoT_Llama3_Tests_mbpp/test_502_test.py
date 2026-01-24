import unittest
from mbpp_502_code import find

class TestFindFunction(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(find(10, 3), 1)
        self.assertEqual(find(15, 4), 3)
        self.assertEqual(find(20, 5), 0)

    def test_negative_integers(self):
        self.assertEqual(find(-10, 3), -1)
        self.assertEqual(find(-15, 4), -3)
        self.assertEqual(find(-20, 5), 0)

    def test_zero(self):
        self.assertEqual(find(0, 3), 0)
        self.assertEqual(find(3, 0), 0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            find('a', 3)
        with self.assertRaises(TypeError):
            find(10, 'b')

    def test_edge_cases(self):
        self.assertEqual(find(0, 0), 0)
        self.assertEqual(find(1, 1), 1)
