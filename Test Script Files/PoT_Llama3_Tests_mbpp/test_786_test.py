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
        self.assertEqual(right_insertion(a, x), 2)

    def test_edge_case_insertion_at_end_with_duplicates(self):
        a = [1, 2, 2, 3, 4, 5]
        x = 5
        self.assertEqual(right_insertion(a, x), 5)

    def test_edge_case_insertion_at_start_with_duplicates(self):
        a = [1, 1, 2, 3, 4, 5]
        x = 0
        self.assertEqual(right_insertion(a, x), 0)

    def test_edge_case_insertion_at_middle_with_duplicates(self):
        a = [1, 1, 2, 2, 3, 4, 5]
        x = 2.5
        self.assertEqual(right_insertion(a, x), 2)

    def test_invalid_input_type(self):
        a = [1, 2, 3, 4, 5]
        x = 'a'
        with self.assertRaises(TypeError):
            right_insertion(a, x)

    def test_invalid_input_value(self):
        a = [1, 2, 3, 4, 5]
        x = None
        with self.assertRaises(TypeError):
            right_insertion(a, x)
