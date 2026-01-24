import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    def test_edge_case(self):
        self.assertEqual(test_three_equal(1, 1, 1), 2)

    def test_boundary_case(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)
        self.assertEqual(test_three_equal(1, 1, 2), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            test_three_equal("a", "b", "c")
