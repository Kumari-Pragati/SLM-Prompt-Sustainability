import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 3), 1)
        self.assertEqual(count_element_in_list(["apple", "banana", "cherry"], "banana"), 1)

    def test_edge_and_boundary(self):
        self.assertEqual(count_element_in_list([], 1), 0)
        self.assertEqual(count_element_in_list([1], 1), 1)
        self.assertEqual(count_element_in_list([1, 1, 1], 1), 3)
        self.assertEqual(count_element_in_list(["apple", "banana", "cherry"], "orange"), 0)

    def test_complex(self):
        self.assertEqual(count_element_in_list([1, 1, 2, 2, 3, 3, 3], 3), 3)
        self.assertEqual(count_element_in_list(["apple", "banana", "cherry", "apple", "banana"], "banana"), 2)
