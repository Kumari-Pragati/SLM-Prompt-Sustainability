import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(position_max([1, 2, 3, 4, 5]), [4])
        self.assertEqual(position_max([-1, -2, -3, -4, -5]), [-5])
        self.assertEqual(position_max([5, 5, 5, 5, 5]), [0, 1, 2, 3, 4])

    def test_edge_cases(self):
        self.assertEqual(position_max([1]), [0])
        self.assertEqual(position_max([-1]), [0])
        self.assertEqual(position_max([5]), [0])

    def test_multiple_max_values(self):
        self.assertEqual(position_max([1, 2, 2, 3, 4]), [1, 2, 3])
        self.assertEqual(position_max([-1, -2, -2, -3, -4]), [-4, -3, -2, -1])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            position_max([])

    def test_single_element_list(self):
        self.assertEqual(position_max([5]), [0])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            position_max("hello")
