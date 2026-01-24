import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):
    def test_breakSum_typical(self):
        self.assertEqual(breakSum(10), 11)

    def test_breakSum_edge(self):
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(2), 1)
        self.assertEqual(breakSum(3), 2)
        self.assertEqual(breakSum(4), 3)
        self.assertEqual(breakSum(5), 4)

    def test_breakSum_max(self):
        self.assertEqual(breakSum(1000000), 1000000)

    def test_breakSum_zero(self):
        self.assertEqual(breakSum(0), 0)
