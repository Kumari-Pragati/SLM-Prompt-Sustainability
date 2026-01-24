import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 2), [1, 2, 3, 5])
        self.assertEqual(remove_kth_element(['a', 'b', 'c', 'd', 'e'], 3), ['a', 'b', 'd', 'e'])

    def test_edge_cases(self):
        self.assertEqual(remove_kth_element([1], 1), [] )
        self.assertEqual(remove_kth_element([1, 2], 0), [] )
        self.assertEqual(remove_kth_element([1, 2], 3), [1, 2] )
        self.assertEqual(remove_kth_element([], 1), [] )

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: remove_kth_element([1, 2], -1))
        self.assertRaises(IndexError, lambda: remove_kth_element([1, 2], 0))

    def test_invalid_input(self):
        self.assertRaises(TypeError, lambda: remove_kth_element('abc', 1))
        self.assertRaises(TypeError, lambda: remove_kth_element([1, 2], 'k') )
