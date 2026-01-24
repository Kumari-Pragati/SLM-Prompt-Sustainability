import unittest
from mbpp_798_code import _sum

class TestSumFunction(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(_sum([1, 2, 3]), 6)
        self.assertEqual(_sum([-1, 0, 1]), 0)
        self.assertEqual(_sum([4, 4, 4]), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(_sum([]), 0)
        self.assertEqual(_sum([0]*1000), 0)
        self.assertEqual(_sum([-1000]), -1000)
        self.assertEqual(_sum([1000]), 1000)
        self.assertEqual(_sum([-1000, 1000]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            _sum(1.23)
        with self.assertRaises(TypeError):
            _sum({"a": 1, "b": 2})
        with self.assertRaises(TypeError):
            _sum(None)
