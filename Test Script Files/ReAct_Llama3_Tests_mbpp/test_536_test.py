import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6], 2), [1, 3, 5])

    def test_edge_case_start(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6], 1), [1, 2, 3, 4, 5, 6])

    def test_edge_case_end(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6], 6), [6])

    def test_edge_case_middle(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6], 3), [1, 4])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            nth_items('abc', 2)

    def test_invalid_input_value(self):
        with self.assertRaises(IndexError):
            nth_items([1, 2, 3], -1)
