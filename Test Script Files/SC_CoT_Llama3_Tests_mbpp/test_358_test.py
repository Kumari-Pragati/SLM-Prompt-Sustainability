import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(moddiv_list([10, 20, 30], [2, 3, 4]), [1, 2, 0])

    def test_edge_cases(self):
        self.assertEqual(moddiv_list([10, 20, 30], [0, 0, 0]), [10, 20, 30])
        self.assertEqual(moddiv_list([10, 20, 30], [1, 1, 1]), [0, 0, 0])

    def test_boundary_cases(self):
        self.assertEqual(moddiv_list([10, 20, 30], [1, 2, 3]), [0, 1, 0])
        self.assertEqual(moddiv_list([10, 20, 30], [4, 5, 6]), [2, 2, 0])

    def test_special_cases(self):
        self.assertEqual(moddiv_list([-10, -20, -30], [2, 3, 4]), [-1, -2, -0])
        self.assertEqual(moddiv_list([10, 20, 30], [-2, -3, -4]), [0, 2, 3])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            moddiv_list("10", [2, 3, 4])
        with self.assertRaises(TypeError):
            moddiv_list([10, 20, 30], "2, 3, 4")
