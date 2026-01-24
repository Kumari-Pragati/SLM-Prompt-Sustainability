import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(is_polite(1), 3)
        self.assertEqual(is_polite(2), 5)
        self.assertEqual(is_polite(3), 7)

    def test_edge_cases(self):
        self.assertEqual(is_polite(-1), 3)
        self.assertEqual(is_polite(0), 2)
        self.assertEqual(is_polite(4), 8)

    def test_boundary_cases(self):
        self.assertEqual(is_polite(1.5), 5)
        self.assertEqual(is_polite(2.5), 7)
        self.assertEqual(is_polite(3.5), 9)

    def test_special_cases(self):
        self.assertEqual(is_polite(math.inf), 3)
        self.assertEqual(is_polite(-math.inf), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_polite("a")
