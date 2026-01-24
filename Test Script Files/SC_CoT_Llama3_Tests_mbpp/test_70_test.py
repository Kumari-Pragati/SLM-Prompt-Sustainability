import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(get_equal([(1, 2), (3, 4), (5, 6)], 2), "All tuples have same length")

    def test_edge_case(self):
        self.assertEqual(get_equal([(1, 2), (3, 4), (5, 6, 7)], 2), "All tuples do not have same length")

    def test_edge_case2(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5, 6)], 3), "All tuples have same length")

    def test_edge_case3(self):
        self.assertEqual(get_equal([(1, 2), (3, 4, 5)], 2), "All tuples do not have same length")

    def test_edge_case4(self):
        self.assertEqual(get_equal([(1, 2, 3, 4), (5, 6, 7, 8)], 4), "All tuples have same length")

    def test_edge_case5(self):
        self.assertEqual(get_equal([(1, 2), (3, 4, 5, 6)], 2), "All tuples do not have same length")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_equal("string", 2)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            get_equal([1, 2, 3], "string")
