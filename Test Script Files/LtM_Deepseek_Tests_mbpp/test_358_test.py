import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(moddiv_list([10, 20, 30], [2, 5, 10]), [0, 4, 0])

    def test_edge_conditions(self):
        self.assertEqual(moddiv_list([], []), [])
        self.assertEqual(moddiv_list([1], [0]), [1])
        self.assertEqual(moddiv_list([10, 20, 30], [2, 5, 0]), [0, 0, 0])

    def test_complex_cases(self):
        self.assertEqual(moddiv_list([10, 20, 30], [2, 5, 10]), [0, 4, 0])
        self.assertEqual(moddiv_list([100, 200, 300], [10, 20, 30]), [0, 0, 0])
