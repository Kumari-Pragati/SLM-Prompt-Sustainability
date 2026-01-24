import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(len(empty_list(5)), 5)
        self.assertEqual(empty_list(0), [])

    def test_edge_condition(self):
        self.assertEqual(len(empty_list(1)), 1)

    def test_boundary_condition(self):
        self.assertEqual(len(empty_list(1000)), 1000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            empty_list("5")
        with self.assertRaises(ValueError):
            empty_list(-5)
