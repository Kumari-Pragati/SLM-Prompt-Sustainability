import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(multi_list(3, 4), [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]])

    def test_edge_condition(self):
        self.assertEqual(multi_list(1, 1), [[0]])

    def test_boundary_condition(self):
        self.assertEqual(multi_list(0, 0), [])
        self.assertEqual(multi_list(1000, 1000), [[0]*1000]*1000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multi_list("3", 4)
        with self.assertRaises(TypeError):
            multi_list(3, "4")
        with self.assertRaises(TypeError):
            multi_list("3", "4")
        with self.assertRaises(ValueError):
            multi_list(-1, 4)
        with self.assertRaises(ValueError):
            multi_list(3, -4)
        with self.assertRaises(ValueError):
            multi_list(-1, -4)
