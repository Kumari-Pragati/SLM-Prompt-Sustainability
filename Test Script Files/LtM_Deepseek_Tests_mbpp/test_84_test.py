import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)

    def test_edge_conditions(self):
        self.assertEqual(sequence(0), 1)
        self.assertEqual(sequence(-1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 4)
        self.assertEqual(sequence(5), 5)
        self.assertEqual(sequence(6), 7)

    def test_complex_cases(self):
        self.assertEqual(sequence(10), 55)
        self.assertEqual(sequence(15), 144)
