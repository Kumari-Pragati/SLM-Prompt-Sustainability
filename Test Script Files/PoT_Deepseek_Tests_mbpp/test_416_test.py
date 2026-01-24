import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(2), 2)
        self.assertEqual(breakSum(3), 2)
        self.assertEqual(breakSum(4), 4)
        self.assertEqual(breakSum(5), 5)
        self.assertEqual(breakSum(6), 6)
        self.assertEqual(breakSum(7), 7)
        self.assertEqual(breakSum(8), 8)
        self.assertEqual(breakSum(9), 9)
        self.assertEqual(breakSum(10), 10)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(1000000), 1000000)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(TypeError):
            breakSum('a')
        with self.assertRaises(ValueError):
            breakSum(-1)
        with self.assertRaises(TypeError):
            breakSum(None)
