import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_lucas(2), 2)
        self.assertEqual(find_lucas(3), 3)
        self.assertEqual(find_lucas(4), 4)

    def test_edge_case(self):
        self.assertEqual(find_lucas(0), 2)
        self.assertEqual(find_lucas(1), 1)

    def test_negative_case(self):
        with self.assertRaises(TypeError):
            find_lucas(-1)

    def test_large_case(self):
        self.assertEqual(find_lucas(10), 55)

    def test_invalid_case(self):
        with self.assertRaises(TypeError):
            find_lucas("a")
