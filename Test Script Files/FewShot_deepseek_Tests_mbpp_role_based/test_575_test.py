import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_no(2, 3, 1, 10), 6)

    def test_boundary_conditions(self):
        self.assertEqual(count_no(2, 3, 1, 1), 1)
        self.assertEqual(count_no(2, 3, 10, 20), 18)

    def test_edge_conditions(self):
        self.assertEqual(count_no(2, 3, 1, 100), 100)
        self.assertEqual(count_no(2, 3, 100, 200), 198)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_no('2', 3, 1, 10)
        with self.assertRaises(TypeError):
            count_no(2, '3', 1, 10)
        with self.assertRaises(TypeError):
            count_no(2, 3, '1', 10)
        with self.assertRaises(TypeError):
            count_no(2, 3, 1, '10')
