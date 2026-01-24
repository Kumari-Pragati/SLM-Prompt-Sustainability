import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(breakSum(2), 1)
        self.assertEqual(breakSum(3), 2)
        self.assertEqual(breakSum(4), 3)

    def test_larger_numbers(self):
        self.assertEqual(breakSum(5), 5)
        self.assertEqual(breakSum(6), 6)
        self.assertEqual(breakSum(7), 7)

    def test_edge_cases(self):
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(1), 1)

    def test_large_numbers(self):
        self.assertEqual(breakSum(1000000), 1000000)
