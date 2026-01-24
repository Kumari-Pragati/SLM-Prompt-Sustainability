import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(minimum(1, 2), 1)
        self.assertEqual(minimum(5, 3), 3)
        self.assertEqual(minimum(10, 10), 10)

    def test_edge_cases(self):
        self.assertEqual(minimum(0, 1), 0)
        self.assertEqual(minimum(-1, 1), -1)
        self.assertEqual(minimum(1, -1), -1)

    def test_boundary_cases(self):
        self.assertEqual(minimum(1, 1), 1)
        self.assertEqual(minimum(-1, -1), -1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            minimum("a", "b")
        with self.assertRaises(TypeError):
            minimum(1, "b")
