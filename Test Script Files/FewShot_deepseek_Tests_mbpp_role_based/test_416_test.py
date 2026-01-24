import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(breakSum(10), 10)
        self.assertEqual(breakSum(20), 20)
        self.assertEqual(breakSum(50), 50)

    def test_edge_conditions(self):
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(breakSum(2), 2)
        self.assertEqual(breakSum(3), 2)
        self.assertEqual(breakSum(4), 4)
        self.assertEqual(breakSum(1000000), 1000000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            breakSum('10')
        with self.assertRaises(ValueError):
            breakSum(-10)
        with self.assertRaises(TypeError):
            breakSum(None)
