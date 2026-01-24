import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(kth_element([2, 3, 1, 5, 4], 5, 3), 3)

    def test_edge_boundary_conditions(self):
        self.assertEqual(kth_element([1], 1, 1), 1)
        self.assertEqual(kth_element([], 0, 0), None)
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 6), None)
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 0), None)

    def test_more_complex_cases(self):
        self.assertEqual(kth_element([10, 20, 30, 40, 50], 5, 3), 30)
        self.assertEqual(kth_element([10, 20, 30, 40, 50], 5, 5), 50)
        self.assertEqual(kth_element([5, 4, 3, 2, 1], 5, 1), 5)
        self.assertEqual(kth_element([5, 4, 3, 2, 1], 5, 5), 1)
