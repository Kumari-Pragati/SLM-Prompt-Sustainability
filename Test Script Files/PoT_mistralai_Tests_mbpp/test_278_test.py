import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_first_elements((1, 2, 3, (4, 5))), 0)
        self.assertEqual(count_first_elements((1, (2, 3), 4)), 0)
        self.assertEqual(count_first_elements((1, (2, 3, (4, 5)))), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_first_elements([]), None)

    def test_edge_case_single_element_not_tuple(self):
        self.assertEqual(count_first_elements((1,)), 0)

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(count_first_elements(((),)), 0)

    def test_edge_case_multiple_tuples_at_start(self):
        self.assertEqual(count_first_elements(((1,), (2, 3))), 0)
        self.assertEqual(count_first_elements(((1,), (2, 3, (4, 5)))), 0)

    def test_edge_case_multiple_tuples_in_middle(self):
        self.assertEqual(count_first_elements((1, (2,), 3, (4, 5))), 1)

    def test_edge_case_multiple_tuples_at_end(self):
        self.assertEqual(count_first_elements((1, 2, (3,), 4, (5,))), 3)
