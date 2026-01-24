import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 3), 2)

    def test_edge_case_smaller(self):
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 0), 0)

    def test_edge_case_larger(self):
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 6), 5)

    def test_edge_case_equal(self):
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 4), 3)

    def test_empty_list(self):
        self.assertEqual(left_insertion([], 1), 0)

    def test_single_element_list(self):
        self.assertEqual(left_insertion([1], 1), 0)
        self.assertEqual(left_insertion([1], 2), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            left_insertion('a', 1)
