import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(2), 2)
        self.assertEqual(breakSum(3), 3)
        self.assertEqual(breakSum(4), 4)

    def test_boundary_conditions(self):
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(MAX), MAX)

    def test_edge_conditions(self):
        self.assertEqual(breakSum(10), 10)
        self.assertEqual(breakSum(15), 15)

    def test_complex_cases(self):
        self.assertEqual(breakSum(100), 100)
        self.assertEqual(breakSum(200), 200)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            breakSum("invalid")
        with self.assertRaises(ValueError):
            breakSum(-1)
