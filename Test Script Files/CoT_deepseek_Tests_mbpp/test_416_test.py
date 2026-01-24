import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(2), 2)
        self.assertEqual(breakSum(10), 10)
        self.assertEqual(breakSum(15), 15)

    def test_edge_cases(self):
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(1000000), 1000000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            breakSum('a')
        with self.assertRaises(TypeError):
            breakSum(None)
        with self.assertRaises(TypeError):
            breakSum([])
        with self.assertRaises(TypeError):
            breakSum({})
        with self.assertRaises(TypeError):
            breakSum(1.5)
        with self.assertRaises(ValueError):
            breakSum(-1)
        with self.assertRaises(ValueError):
            breakSum(1000001)
