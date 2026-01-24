import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(2), 1)
        self.assertEqual(breakSum(3), 1)
        self.assertEqual(breakSum(4), 2)
        self.assertEqual(breakSum(5), 2)
        self.assertEqual(breakSum(6), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(MAX), MAX)
        self.assertEqual(breakSum(100000), 100000)
        self.assertEqual(breakSum(100001), 100001)

    def test_complex_inputs(self):
        self.assertEqual(breakSum(7), 3)
        self.assertEqual(breakSum(8), 3)
        self.assertEqual(breakSum(9), 4)
        self.assertEqual(breakSum(10), 5)
        self.assertEqual(breakSum(11), 5)
        self.assertEqual(breakSum(12), 6)
        self.assertEqual(breakSum(13), 6)
        self.assertEqual(breakSum(14), 7)
        self.assertEqual(breakSum(15), 7)
        self.assertEqual(breakSum(16), 8)
        self.assertEqual(breakSum(17), 8)
        self.assertEqual(breakSum(18), 9)
        self.assertEqual(breakSum(19), 9)
        self.assertEqual(breakSum(20), 10)
