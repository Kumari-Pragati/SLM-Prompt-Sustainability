import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):
    def test_typical_use_cases(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 4)
        self.assertEqual(sequence(5), 5)
        self.assertEqual(sequence(6), 7)

    def test_edge_conditions(self):
        self.assertEqual(sequence(0), 1)
        self.assertEqual(sequence(-1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(sequence(30), 102334155)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sequence('a')
        with self.assertRaises(TypeError):
            sequence(None)
        with self.assertRaises(TypeError):
            sequence([])
