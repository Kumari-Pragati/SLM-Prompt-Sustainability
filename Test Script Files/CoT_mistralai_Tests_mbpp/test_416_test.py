import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(breakSum(5), 2)
        self.assertEqual(breakSum(7), 2)
        self.assertEqual(breakSum(9), 3)
        self.assertEqual(breakSum(10), 3)
        self.assertEqual(breakSum(17), 4)
        self.assertEqual(breakSum(20), 5)
        self.assertEqual(breakSum(100), 7)
        self.assertEqual(breakSum(1000), 10)
        self.assertEqual(breakSum(10000), 13)
        self.assertEqual(breakSum(100000), 16)
        self.assertEqual(breakSum(1000000), 19)

    def test_edge_cases(self):
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(2), 1)
        self.assertEqual(breakSum(3), 2)

    def test_boundary_conditions(self):
        self.assertEqual(breakSum(MAX), breakSum(MAX - 1))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, breakSum, -1)
        self.assertRaises(ValueError, breakSum, MAX + 1)
        self.assertRaises(ValueError, breakSum, float('inf'))
        self.assertRaises(ValueError, breakSum, complex(0, 0))
        self.assertRaises(ValueError, breakSum, 'str')
