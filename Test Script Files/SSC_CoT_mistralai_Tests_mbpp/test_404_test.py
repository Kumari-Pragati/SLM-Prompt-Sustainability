import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(minimum(1, 2), 1)
        self.assertEqual(minimum(2, 1), 1)
        self.assertEqual(minimum(-1, -2), -1)
        self.assertEqual(minimum(-2, -1), -2)

    def test_edge_cases(self):
        self.assertEqual(minimum(0, 1), 0)
        self.assertEqual(minimum(1, 0), 0)
        self.assertEqual(minimum(-0, -1), -0)
        self.assertEqual(minimum(-1, -0), -1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, minimum, "a", "b")
        self.assertRaises(TypeError, minimum, 1.5, "b")
