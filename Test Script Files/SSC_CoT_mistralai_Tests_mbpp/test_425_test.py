import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 2, 2], 2), 3)
        self.assertEqual(count_element_in_list(["apple", "banana", "apple"], "apple"), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_element_in_list([], 1), 0)
        self.assertEqual(count_element_in_list([1], 1), 1)
        self.assertEqual(count_element_in_list([1, 1, 1], 1), 3)
        self.assertEqual(count_element_in_list(["apple", "banana"], "apple"), 1)
        self.assertEqual(count_element_in_list(["apple", "banana"], "orange"), 0)

    def test_special_cases(self):
        self.assertEqual(count_element_in_list([1, 1, 1, 1, 2], 1), 4)
        self.assertEqual(count_element_in_list([1, 1, 1, "two"], 1), 3)
