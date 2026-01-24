import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_tuplex((1, 2, 3, 2, 4, 2), 2), 3)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_tuplex((), 1), 0)

    def test_boundary_case_single_element_tuple(self):
        self.assertEqual(count_tuplex((1,), 1), 1)
        self.assertEqual(count_tuplex((1,), 2), 0)

    def test_corner_case_repeated_elements(self):
        self.assertEqual(count_tuplex((1, 2, 2, 3, 3, 3), 3), 3)

    def test_corner_case_large_tuple(self):
        large_tuple = tuple(range(1, 10001))
        self.assertEqual(count_tuplex(large_tuple, 5000), 1)

    def test_corner_case_large_tuple_repeated_value(self):
        large_tuple = tuple(range(1, 10001)) * 2
        self.assertEqual(count_tuplex(large_tuple, 5000), 20000)
