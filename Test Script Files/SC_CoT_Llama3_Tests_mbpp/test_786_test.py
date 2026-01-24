import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):

    def test_typical_case(self):
        a = [1, 2, 3, 4, 5]
        x = 3
        self.assertEqual(right_insertion(a, x), 2)

    def test_edge_case_lower(self):
        a = [1, 2, 3, 4, 5]
        x = 1
        self.assertEqual(right_insertion(a, x), 0)

    def test_edge_case_higher(self):
        a = [1, 2, 3, 4, 5]
        x = 6
        self.assertEqual(right_insertion(a, x), 5)

    def test_edge_case_equal(self):
        a = [1, 2, 3, 4, 5]
        x = 4
        self.assertEqual(right_insertion(a, x), 3)

    def test_empty_list(self):
        a = []
        x = 1
        self.assertEqual(right_insertion(a, x), 0)

    def test_single_element_list(self):
        a = [1]
        x = 1
        self.assertEqual(right_insertion(a, x), 0)

    def test_single_element_list_edge(self):
        a = [1]
        x = 2
        self.assertEqual(right_insertion(a, x), 1)

    def test_multiple_edge_cases(self):
        a = [1, 2, 3, 4, 5]
        x = 1
        self.assertEqual(right_insertion(a, x), 0)
        x = 2
        self.assertEqual(right_insertion(a, x), 1)
        x = 3
        self.assertEqual(right_insertion(a, x), 2)
        x = 4
        self.assertEqual(right_insertion(a, x), 3)
        x = 5
        self.assertEqual(right_insertion(a, x), 4)
        x = 6
        self.assertEqual(right_insertion(a, x), 5)
