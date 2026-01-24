import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_lucas(0), 2)
        self.assertEqual(find_lucas(1), 1)

    def test_edge_conditions(self):
        self.assertEqual(find_lucas(-1), 1)
        self.assertEqual(find_lucas(-2), 2)
        self.assertEqual(find_lucas(-3), 3)

    def test_complex_cases(self):
        self.assertEqual(find_lucas(2), 3)
        self.assertEqual(find_lucas(3), 4)
        self.assertEqual(find_lucas(4), 7)
        self.assertEqual(find_lucas(5), 11)
