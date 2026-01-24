import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(minimum(3, 5), 3)

    def test_edge_condition(self):
        self.assertEqual(minimum(0, 0), 0)

    def test_boundary_condition(self):
        self.assertEqual(minimum(-10, 10), -10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            minimum("a", 1)
