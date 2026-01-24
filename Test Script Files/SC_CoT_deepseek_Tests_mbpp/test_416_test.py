import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(breakSum(10), 10)
        self.assertEqual(breakSum(20), 20)
        self.assertEqual(breakSum(50), 50)

    def test_boundary_conditions(self):
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(MAX), MAX)

    def test_edge_cases(self):
        self.assertEqual(breakSum(2), 2)
        self.assertEqual(breakSum(3), 2)
        self.assertEqual(breakSum(4), 4)
        self.assertEqual(breakSum(5), 5)
        self.assertEqual(breakSum(6), 6)
        self.assertEqual(breakSum(7), 7)
        self.assertEqual(breakSum(8), 8)
        self.assertEqual(breakSum(9), 9)
        self.assertEqual(breakSum(10), 10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            breakSum('10')
        with self.assertRaises(TypeError):
            breakSum(-10)
        with self.assertRaises(TypeError):
            breakSum(10.5)
