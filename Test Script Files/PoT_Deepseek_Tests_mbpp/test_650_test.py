import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 4], 3, 3))

    def test_edge_cases(self):
        self.assertFalse(are_Equal([], [1], 0, 1))
        self.assertFalse(are_Equal([1], [], 1, 0))
        self.assertFalse(are_Equal([], [], 0, 0))

    def test_boundary_conditions(self):
        self.assertTrue(are_Equal([1], [1], 1, 1))
        self.assertFalse(are_Equal([1], [2], 1, 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            are_Equal([1, 2, 3], [1, 2, 3], '3', 3)
        with self.assertRaises(TypeError):
            are_Equal([1, 2, 3], [1, 2, 3], 3, '3')
        with self.assertRaises(TypeError):
            are_Equal([1, 2, 3], [1, 2, '3'], 3, 3)
