import unittest
from mbpp_404_code import minimum

class TestMinimumFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(minimum(5, 10), 5)
        self.assertEqual(minimum(15, 10), 10)

    def test_edge_cases(self):
        self.assertEqual(minimum(0, 0), 0)
        self.assertEqual(minimum(-5, -10), -10)
        self.assertEqual(minimum(-5, 0), -5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            minimum("5", 10)
        with self.assertRaises(TypeError):
            minimum(5, "10")
        with self.assertRaises(TypeError):
            minimum("5", "10")
