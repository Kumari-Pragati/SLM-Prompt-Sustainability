import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 5), 2)

    def test_edge_condition(self):
        self.assertEqual(left_insertion([], 5), 0)

    def test_boundary_condition(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 1), 0)
        self.assertEqual(left_insertion([1, 3, 5, 7], 7), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            left_insertion("not a list", 5)
