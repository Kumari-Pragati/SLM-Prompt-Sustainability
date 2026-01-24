import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):
    def test_typical_use_case(self):
        a = [1, 2, 3, 4, 5]
        x = 3
        self.assertEqual(right_insertion(a, x), 2)

    def test_edge_case_empty_list(self):
        a = []
        x = 1
        self.assertEqual(right_insertion(a, x), 0)

    def test_edge_case_single_element_list(self):
        a = [1]
        x = 1
        self.assertEqual(right_insertion(a, x), 0)
        x = 2
        self.assertEqual(right_insertion(a, x), 1)

    def test_edge_case_x_is_in_a(self):
        a = [1, 2, 3, 4, 5]
        x = 4
        self.assertEqual(right_insertion(a, x), 3)

    def test_edge_case_x_is_not_in_a(self):
        a = [1, 2, 3, 4, 5]
        x = 6
        self.assertEqual(right_insertion(a, x), 4)

    def test_invalid_input_non_list(self):
        a = "hello"
        x = 1
        with self.assertRaises(TypeError):
            right_insertion(a, x)
