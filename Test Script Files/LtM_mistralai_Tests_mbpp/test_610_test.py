import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 2), [1, 2, 3, 5])
        self.assertEqual(remove_kth_element([1], 1), [])
        self.assertEqual(remove_kth_element([1, 2], 1), [2])
        self.assertEqual(remove_kth_element([1, 2, 3], 0), [2, 3])
        self.assertEqual(remove_kth_element([1, 2, 3], 3), [1, 2])

    def test_edge_and_boundary(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 0), [2, 3])
        self.assertEqual(remove_kth_element([1, 2, 3], len([1, 2, 3])), [1])
        self.assertEqual(remove_kth_element([], 0), [])
        self.assertEqual(remove_kth_element([1], 0), [])
        self.assertEqual(remove_kth_element([1], 1), [])

    def test_complex(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 2, 1], 2), [1, 3, 2, 1])
        self.assertEqual(remove_kth_element([1, 2, 3, 2, 1], 4), [1, 2, 3])
        self.assertEqual(remove_kth_element([1, 2, 3, 2, 1], 0), [2, 3, 2, 1])
        self.assertEqual(remove_kth_element([1, 2, 3, 2, 1], 5), [1, 2, 3, 2])
