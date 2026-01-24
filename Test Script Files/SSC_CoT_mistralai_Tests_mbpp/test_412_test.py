import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_normal_input(self):
        self.assertListEqual(remove_odd([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertListEqual(remove_odd([2, 4, 6]), [])
        self.assertListEqual(remove_odd([4, 4, 4]), [])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(remove_odd([0]), [])
        self.assertListEqual(remove_odd([1]), [])
        self.assertListEqual(remove_odd([-1]), [])
        self.assertListEqual(remove_odd([-2]), [])
        self.assertListEqual(remove_odd([float('inf')]), [])
        self.assertListEqual(remove_odd([-float('inf')]), [])
        self.assertListEqual(remove_odd([None]), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            remove_odd(1.23)
        with self.assertRaises(TypeError):
            remove_odd(("str",))
        with self.assertRaises(TypeError):
            remove_odd([1, 2, 3], 4)
