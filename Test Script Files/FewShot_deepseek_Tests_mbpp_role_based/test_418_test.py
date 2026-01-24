import unittest
from mbpp_418_code import Find_Max

class TestFindMax(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_edge_condition(self):
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -1)

    def test_boundary_condition(self):
        self.assertEqual(Find_Max([0]), 0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            Find_Max([])

    def test_single_element_list(self):
        self.assertEqual(Find_Max([1]), 1)
