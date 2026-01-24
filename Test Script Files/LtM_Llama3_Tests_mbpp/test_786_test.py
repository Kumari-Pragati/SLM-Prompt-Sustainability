import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(right_insertion([], 5), 0)

    def test_single_element_input(self):
        self.assertEqual(right_insertion([1], 5), 1)

    def test_insertion_at_start(self):
        self.assertEqual(right_insertion([1, 2, 3], 0), 0)

    def test_insertion_at_end(self):
        self.assertEqual(right_insertion([1, 2, 3], 4), 3)

    def test_insertion_between_elements(self):
        self.assertEqual(right_insertion([1, 2, 3], 2), 1)

    def test_insertion_at_max_value(self):
        self.assertEqual(right_insertion([1, 2, 3], 3), 2)

    def test_insertion_at_min_value(self):
        self.assertEqual(right_insertion([1, 2, 3], 1), 0)

    def test_insertion_at_max_value_edge_case(self):
        self.assertEqual(right_insertion([1, 2, 3], 3.9), 2)

    def test_insertion_at_min_value_edge_case(self):
        self.assertEqual(right_insertion([1, 2, 3], 0.9), 0)
