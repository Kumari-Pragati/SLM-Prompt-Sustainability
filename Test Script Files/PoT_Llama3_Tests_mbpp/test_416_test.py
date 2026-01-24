import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(breakSum(10), 11)

    def test_edge_case(self):
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(2), 1)
        self.assertEqual(breakSum(3), 2)
        self.assertEqual(breakSum(4), 3)
        self.assertEqual(breakSum(5), 4)

    def test_boundary_case(self):
        self.assertEqual(breakSum(1000000), 1000000)

    def test_tricky_branch(self):
        self.assertEqual(breakSum(6), 6)
