import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(increment_numerics([1, 2, 3], 1), [2, 3, 4])
        self.assertEqual(increment_numerics(["1", "2", "3"], 1), ["2", "3", "4"])
        self.assertEqual(increment_numerics(["1a", "2b", "3c"], 1), ["2a", "3b", "4c"])

    def test_edge_and_boundary(self):
        self.assertEqual(increment_numerics([0, -1], 1), [1, -1])
        self.assertEqual(increment_numerics([9], 1), [10])
        self.assertEqual(increment_numerics(["-1"], 1), ["0"])
        self.assertEqual(increment_numerics(["9"], 1), ["10"])
        self.assertEqual(increment_numerics([10], 1), [11])
        self.assertEqual(increment_numerics(["-10"], 1), ["-9"])

    def test_complex(self):
        self.assertEqual(increment_numerics(["1a", "2b", "3c", "4d"], 1), ["2a", "3b", "4c", "5d"])
        self.assertEqual(increment_numerics(["1", "2", "3", "4"], -1), ["0", "1", "2", "3"])
        self.assertEqual(increment_numerics(["-1", "-2", "-3"], -1), ["0", "1", "2"])
