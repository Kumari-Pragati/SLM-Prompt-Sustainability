import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):

    def test_breakSum_typical(self):
        self.assertEqual(breakSum(2), 1)
        self.assertEqual(breakSum(3), 2)
        self.assertEqual(breakSum(4), 3)
        self.assertEqual(breakSum(5), 4)
        self.assertEqual(breakSum(6), 6)
        self.assertEqual(breakSum(7), 7)
        self.assertEqual(breakSum(8), 8)
        self.assertEqual(breakSum(9), 9)
        self.assertEqual(breakSum(10), 10)

    def test_breakSum_edge(self):
        self.assertEqual(breakSum(1), 0)
        self.assertEqual(breakSum(11), 11)
        self.assertEqual(breakSum(12), 12)
        self.assertEqual(breakSum(13), 13)
        self.assertEqual(breakSum(14), 14)
        self.assertEqual(breakSum(15), 15)

    def test_breakSum_special(self):
        self.assertEqual(breakSum(1000000), 1000000)
        self.assertEqual(breakSum(100000), 100000)
        self.assertEqual(breakSum(10000), 10000)
        self.assertEqual(breakSum(1000), 1000)
        self.assertEqual(breakSum(100), 100)

    def test_breakSum_invalid(self):
        with self.assertRaises(TypeError):
            breakSum("a")
        with self.assertRaises(TypeError):
            breakSum(None)
        with self.assertRaises(TypeError):
            breakSum(1.5)
