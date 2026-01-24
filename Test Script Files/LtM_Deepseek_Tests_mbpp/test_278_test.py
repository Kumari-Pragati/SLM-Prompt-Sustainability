import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_first_elements((1, 2, 3)), 3)

    def test_edge_condition_empty_input(self):
        self.assertEqual(count_first_elements(()), 0)

    def test_edge_condition_single_tuple_input(self):
        self.assertEqual(count_first_elements(()), 0)
        self.assertEqual(count_first_elements(((),)), 1)

    def test_complex_input(self):
        self.assertEqual(count_first_elements((1, (2, 3), 4)), 2)
