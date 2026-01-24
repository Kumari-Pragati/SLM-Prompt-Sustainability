import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4, 5)), ((1, 5)))

    def test_edge_condition(self):
        self.assertEqual(front_and_rear(()), ((),))

    def test_boundary_condition(self):
        self.assertEqual(front_and_rear((1,)), ((1, 1)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            front_and_rear("1, 2, 3")
