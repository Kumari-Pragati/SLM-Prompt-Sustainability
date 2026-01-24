import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(breakSum(3), 1)
        self.assertEqual(breakSum(7), 2)
        self.assertEqual(breakSum(10), 3)
        self.assertEqual(breakSum(20), 4)
        self.assertEqual(breakSum(100), 8)
        self.assertEqual(breakSum(1000), 17)
        self.assertEqual(breakSum(10000), 43)
        self.assertEqual(breakSum(100000), 102)
        self.assertEqual(breakSum(1000000), 232)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(2), 1)
        self.assertEqual(breakSum(MAX), 232)
        self.assertEqual(breakSum(MAX + 1), 233)

    def test_special_cases(self):
        self.assertEqual(breakSum(4), 2)
        self.assertEqual(breakSum(6), 2)
        self.assertEqual(breakSum(8), 3)
        self.assertEqual(breakSum(9), 3)
        self.assertEqual(breakSum(12), 4)
        self.assertEqual(breakSum(15), 4)
        self.assertEqual(breakSum(16), 5)
        self.assertEqual(breakSum(24), 6)
        self.assertEqual(breakSum(27), 6)
        self.assertEqual(breakSum(36), 7)
        self.assertEqual(breakSum(48), 8)
