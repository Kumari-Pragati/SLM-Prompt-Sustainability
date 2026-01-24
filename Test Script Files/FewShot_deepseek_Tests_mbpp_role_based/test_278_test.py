import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_first_elements((1, 2, (3, 4))), 1)

    def test_edge_condition(self):
        self.assertEqual(count_first_elements(()), 0)

    def test_boundary_condition(self):
        self.assertEqual(count_first_elements((1,)), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_first_elements(1)
