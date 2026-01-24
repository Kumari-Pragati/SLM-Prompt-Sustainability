import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(index_minimum([(1, 2), (3, 1), (2, 3), (4, 2)]), (1, 2))
        self.assertEqual(index_minimum([(0, 0), (1, 1), (2, 2), (3, 3)]), (0, 0))

    def test_edge_cases(self):
        self.assertEqual(index_minimum([(1, 2), (1, 1), (2, 3), (4, 2)]), (1, 1))
        self.assertEqual(index_minimum([(1, 2), (1, 1), (2, 3), (1, 2)]), (1, 1))
        self.assertEqual(index_minimum([(1, 2), (1, 1), (2, 3), (1, 2), (1, 1)]), (1, 1))

    def test_empty_list(self):
        self.assertIsNone(index_minimum([]))

    def test_single_element(self):
        self.assertEqual(index_minimum([(1, 2)]), (1, 2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            index_minimum("not a list")
        with self.assertRaises(TypeError):
            index_minimum([1])
