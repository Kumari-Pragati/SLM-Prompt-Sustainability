import unittest

from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_lucas(0), 2)
        self.assertEqual(find_lucas(1), 1)
        self.assertEqual(find_lucas(5), 11)

    def test_edge_cases(self):
        self.assertEqual(find_lucas(-1), 2)
        self.assertEqual(find_lucas(-10), 2)

    def test_corner_cases(self):
        self.assertEqual(find_lucas(20), 10946)

    def test_invalid_inputs(self):
        with self.assertRaises(RecursionError):
            find_lucas(30)
