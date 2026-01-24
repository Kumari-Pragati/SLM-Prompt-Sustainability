import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_typical_inputs(self):
        result = multi_list(3, 4)
        self.assertEqual(result, [[0, 0, 0, 0], [0, 1, 2, 3], [3, 6, 9, 12]])

    def test_edge_cases(self):
        result = multi_list(0, 4)
        self.assertEqual(result, [[0, 0, 0, 0]])
        result = multi_list(4, 0)
        self.assertEqual(result, [[0]])

    def test_boundary_cases(self):
        result = multi_list(1, 4)
        self.assertEqual(result, [[0, 0, 0, 0]])
        result = multi_list(4, 1)
        self.assertEqual(result, [[0]])

    def test_special_cases(self):
        result = multi_list(-1, 4)
        self.assertEqual(result, [])
        result = multi_list(4, -1)
        self.assertEqual(result, [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            multi_list('a', 4)
        with self.assertRaises(TypeError):
            multi_list(4, 'a')
