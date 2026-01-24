import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 3), 3)
        self.assertEqual(kth_element([10, 9, 8, 7, 6], 5, 2), 9)
        self.assertEqual(kth_element([5, 4, 3, 2, 1], 5, 1), 1)

    def test_edge_and_boundary(self):
        self.assertEqual(kth_element([], 1, 1), None)
        self.assertEqual(kth_element([1], 1, 1), 1)
        self.assertEqual(kth_element([1], 2, 1), None)
        self.assertEqual(kth_element([1], 2, 2), 1)
        self.assertEqual(kth_element([1], 3, 1), None)
        self.assertEqual(kth_element([1], 3, 2), None)
        self.assertEqual(kth_element([1], 3, 3), 1)

        self.assertEqual(kth_element([1, 2], 2, 1), 1)
        self.assertEqual(kth_element([1, 2], 2, 2), 2)

        self.assertEqual(kth_element([1, 2, 3], 3, 1), 1)
        self.assertEqual(kth_element([1, 2, 3], 3, 2), 2)
        self.assertEqual(kth_element([1, 2, 3], 3, 3), 3)

    def test_complex(self):
        self.assertEqual(kth_element([1, 2, 3, 2, 1], 5, 3), 2)
        self.assertEqual(kth_element([1, 2, 3, 2, 1], 5, 5), 1)
