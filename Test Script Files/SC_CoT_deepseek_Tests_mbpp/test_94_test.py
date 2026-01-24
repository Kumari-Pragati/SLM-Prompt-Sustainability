import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(index_minimum([(1, 2), (2, 1), (3, 2)]), 2)

    def test_edge_case(self):
        self.assertEqual(index_minimum([(1, 1), (2, 2), (3, 3)]), 1)

    def test_boundary_case(self):
        self.assertEqual(index_minimum([(1, 0), (2, 0), (3, 0)]), 1)

    def test_special_case(self):
        self.assertEqual(index_minimum([(1, -1), (2, -2), (3, -3)]), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            index_minimum("not a list")
