import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_no(2, 3, 1, 5), 4)

    def test_boundary_conditions(self):
        self.assertEqual(count_no(1, 0, 1, 1), 1)
        self.assertEqual(count_no(1, 1, 1, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(count_no(1, 10, 10, 20), 15)
        self.assertEqual(count_no(2, 5, 10, 20), 12)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            count_no(0, 3, 1, 5)
        with self.assertRaises(Exception):
            count_no(1, -3, 1, 5)
        with self.assertRaises(Exception):
            count_no(1, 3, 0, 5)
        with self.assertRaises(Exception):
            count_no(1, 3, 1, 0)
        with self.assertRaises(Exception):
            count_no(1, 3, 5, 1)
