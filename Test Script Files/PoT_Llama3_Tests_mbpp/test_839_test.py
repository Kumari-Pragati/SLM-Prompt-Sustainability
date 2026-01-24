import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_tuple([(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4), (5, 6)])

    def test_edge_case(self):
        self.assertEqual(sort_tuple([(5, 2), (3, 4), (1, 6)]), [(1, 6), (3, 4), (5, 2)])

    def test_edge_case2(self):
        self.assertEqual(sort_tuple([(1, 2), (2, 3), (3, 1)]), [(1, 2), (2, 3), (3, 1)])

    def test_edge_case3(self):
        self.assertEqual(sort_tuple([(1, 2), (1, 3), (2, 1)]), [(1, 1), (1, 2), (2, 1)])

    def test_empty_input(self):
        self.assertEqual(sort_tuple([]), [])

    def test_single_element_input(self):
        self.assertEqual(sort_tuple([(1, 2)]), [(1, 2)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_tuple("Invalid input")
