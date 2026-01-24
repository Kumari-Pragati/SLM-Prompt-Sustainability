import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(multi_list(3, 3), [[0, 0, 0], [0, 1, 2], [3, 6, 9]])

    def test_edge_cases(self):
        self.assertEqual(multi_list(0, 0), [])
        self.assertEqual(multi_list(1, 0), [])
        self.assertEqual(multi_list(0, 1), [[]])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            multi_list('a', 3)
        with self.assertRaises(TypeError):
            multi_list(3, 'a')

    def test_boundary_conditions(self):
        self.assertEqual(multi_list(1, 1), [[0]])
        self.assertEqual(multi_list(2, 2), [[0, 0], [0, 1]])
