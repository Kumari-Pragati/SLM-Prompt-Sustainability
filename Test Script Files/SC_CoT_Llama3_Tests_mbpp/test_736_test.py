import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_typical_input(self):
        a = [1, 2, 3, 4, 5]
        x = 3
        self.assertEqual(left_insertion(a, x), 2)

    def test_edge_case_lower(self):
        a = [1, 2, 3, 4, 5]
        x = 1
        self.assertEqual(left_insertion(a, x), 0)

    def test_edge_case_higher(self):
        a = [1, 2, 3, 4, 5]
        x = 6
        self.assertEqual(left_insertion(a, x), 5)

    def test_edge_case_equal(self):
        a = [1, 2, 3, 4, 5]
        x = 3
        self.assertEqual(left_insertion(a, x), 2)

    def test_empty_list(self):
        a = []
        x = 1
        self.assertEqual(left_insertion(a, x), 0)

    def test_single_element_list(self):
        a = [1]
        x = 1
        self.assertEqual(left_insertion(a, x), 0)

    def test_single_element_list_edge_case_lower(self):
        a = [1]
        x = 0
        self.assertEqual(left_insertion(a, x), 0)

    def test_single_element_list_edge_case_higher(self):
        a = [1]
        x = 2
        self.assertEqual(left_insertion(a, x), 1)

    def test_invalid_input_type(self):
        a = [1, 2, 3, 4, 5]
        x = 'a'
        with self.assertRaises(TypeError):
            left_insertion(a, x)

    def test_invalid_input_type_edge_case(self):
        a = [1, 2, 3, 4, 5]
        x = None
        with self.assertRaises(TypeError):
            left_insertion(a, x)
