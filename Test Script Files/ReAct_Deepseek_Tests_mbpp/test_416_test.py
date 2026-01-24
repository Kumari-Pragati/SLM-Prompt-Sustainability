import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(2), 2)
        self.assertEqual(breakSum(3), 2)
        self.assertEqual(breakSum(4), 4)
        self.assertEqual(breakSum(5), 5)
        self.assertEqual(breakSum(10), 10)
        self.assertEqual(breakSum(15), 15)
        self.assertEqual(breakSum(20), 20)

    def test_edge_cases(self):
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(1000000), 1000000)

    def test_boundary_cases(self):
        self.assertEqual(breakSum(21), 21)
        self.assertEqual(breakSum(22), 22)
        self.assertEqual(breakSum(23), 23)
        self.assertEqual(breakSum(24), 24)
        self.assertEqual(breakSum(25), 25)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            breakSum('a')
        with self.assertRaises(ValueError):
            breakSum(-1)
