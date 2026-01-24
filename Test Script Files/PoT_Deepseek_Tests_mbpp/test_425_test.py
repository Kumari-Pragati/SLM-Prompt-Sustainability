import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 3), 1)
        self.assertEqual(count_element_in_list(['a', 'b', 'c', 'd', 'e'], 'c'), 1)

    def test_edge_case(self):
        self.assertEqual(count_element_in_list([], 1), 0)
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 6), 0)

    def test_boundary_case(self):
        self.assertEqual(count_element_in_list([1], 1), 1)
        self.assertEqual(count_element_in_list(['a'], 'a'), 1)

    def test_corner_case(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 4, 5], 2), 2)
        self.assertEqual(count_element_in_list(['a', 'b', 'b', 'c', 'd', 'e'], 'b'), 2)
