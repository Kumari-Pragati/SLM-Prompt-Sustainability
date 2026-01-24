import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Operations(2, 3), 2)

    def test_typical_case_2(self):
        self.assertEqual(min_Operations(5, 10), 1)

    def test_boundary_condition(self):
        self.assertEqual(min_Operations(0, 10), 9)

    def test_boundary_condition_2(self):
        self.assertEqual(min_Operations(10, 0), 9)

    def test_edge_case(self):
        self.assertEqual(min_Operations(1, 1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Operations("2", 3)

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            min_Operations(2, "3")

    def test_invalid_input_3(self):
        with self.assertRaises(TypeError):
            min_Operations("2", "3")
