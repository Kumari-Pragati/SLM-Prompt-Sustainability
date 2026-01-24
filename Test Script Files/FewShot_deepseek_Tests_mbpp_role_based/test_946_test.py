import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2), [(4, 4), (3, 3)])

    def test_edge_case(self):
        self.assertEqual(most_common_elem([], 1), [])

    def test_boundary_condition(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 10), [(4, 4), (3, 3), (2, 2), (1, 1)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            most_common_elem("string", 1)
