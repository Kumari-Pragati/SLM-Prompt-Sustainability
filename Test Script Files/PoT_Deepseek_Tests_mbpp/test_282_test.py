import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])
        self.assertEqual(sub_list([10, 20, 30], [5, 10, 15]), [5, 10, 15])

    def test_edge_cases(self):
        self.assertEqual(sub_list([], []), [])
        self.assertEqual(sub_list([1], [0]), [1])

    def test_boundary_conditions(self):
        self.assertEqual(sub_list([0]*10000, [0]*10000), [0]*10000)
        self.assertEqual(sub_list([1000]*10000, [-1000]*10000), [2000]*10000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sub_list("1,2,3", [1, 2, 3])
        with self.assertRaises(TypeError):
            sub_list([1, 2, 3], "1,2,3")
        with self.assertRaises(TypeError):
            sub_list("1,2,3", "1,2,3")
