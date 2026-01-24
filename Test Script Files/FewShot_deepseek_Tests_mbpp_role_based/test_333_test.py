import unittest
from mbpp_333_code import Sort

class TestSort(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Sort([(2, 3), (1, 2), (4, 1)]), [(4, 1), (2, 3), (1, 2)])

    def test_edge_condition(self):
        self.assertEqual(Sort([(2, 3), (1, 2), (4, 1), (2, 2)]), [(4, 1), (2, 2), (2, 3), (1, 2)])

    def test_boundary_condition(self):
        self.assertEqual(Sort([(2, 3), (1, 2), (4, 1), (2, 2), (2, 3)]), [(4, 1), (2, 2), (2, 3), (2, 3), (1, 2)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Sort([1, 2, 3])
