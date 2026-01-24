import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(breakSum(2), 1)
        self.assertEqual(breakSum(3), 2)
        self.assertEqual(breakSum(4), 3)
        self.assertEqual(breakSum(5), 4)
        self.assertEqual(breakSum(6), 6)

    def test_edge(self):
        self.assertEqual(breakSum(1), 0)
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(MAX), MAX)

    def test_breakSum(self):
        self.assertEqual(breakSum(10), 10)
        self.assertEqual(breakSum(11), 11)
        self.assertEqual(breakSum(12), 11)
        self.assertEqual(breakSum(13), 12)
        self.assertEqual(breakSum(14), 13)

    def test_breakSum2(self):
        self.assertEqual(breakSum(15), 15)
        self.assertEqual(breakSum(16), 15)
        self.assertEqual(breakSum(17), 16)
        self.assertEqual(breakSum(18), 17)
        self.assertEqual(breakSum(19), 18)
