import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):
    def test_typical_case(self):
        a = [1, 2, 3, 4, 5]
        x = 3
        self.assertEqual(right_insertion(a, x), 2)

    def test_edge_case_insertion_at_start(self):
        a = [1, 2, 3, 4, 5]
        x = 0
        self.assertEqual(right_insertion(a, x), 0)

    def test_edge_case_insertion_at_end(self):
        a = [1, 2, 3, 4, 5]
        x = 6
        self.assertEqual(right_insertion(a, x), 5)

    def test_edge_case_insertion_at_middle(self):
        a = [1, 2, 3, 4, 5]
        x = 3.5
        self.assertRaises(TypeError, right_insertion, a, x)

    def test_edge_case_empty_list(self):
        a = []
        x = 1
        self.assertEqual(right_insertion(a, x), 0)

    def test_edge_case_single_element_list(self):
        a = [1]
        x = 1
        self.assertEqual(right_insertion(a, x), 0)

    def test_edge_case_single_element_list_insertion_at_start(self):
        a = [1]
        x = 0
        self.assertEqual(right_insertion(a, x), 0)

    def test_edge_case_single_element_list_insertion_at_end(self):
        a = [1]
        x = 2
        self.assertEqual(right_insertion(a, x), 1)

    def test_edge_case_single_element_list_insertion_at_middle(self):
        a = [1]
        x = 1.5
        self.assertRaises(TypeError, right_insertion, a, x)
