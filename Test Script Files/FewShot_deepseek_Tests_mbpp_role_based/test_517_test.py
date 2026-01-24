import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)

    def test_edge_condition(self):
        self.assertEqual(largest_pos([0]), 0)

    def test_boundary_condition(self):
        self.assertEqual(largest_pos([-1, -2, -3, -4, -5]), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            largest_pos("1, 2, 3, 4, 5")

        with self.assertRaises(TypeError):
            largest_pos(12345)

        with self.assertRaises(TypeError):
            largest_pos(None)

        with self.assertRaises(TypeError):
            largest_pos([])

        with self.assertRaises(TypeError):
            largest_pos([1, "2", 3, 4, 5])

        with self.assertRaises(TypeError):
            largest_pos([1, None, 3, 4, 5])
