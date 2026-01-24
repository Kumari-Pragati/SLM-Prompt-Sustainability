import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 5, 10), [10, 20, 30, 40])

    def test_edge_case(self):
        self.assertEqual(div_of_nums([15, 30, 45, 60], 3, 5), [15, 30, 45, 60])

    def test_boundary_case(self):
        self.assertEqual(div_of_nums([100, 200, 300, 400], 100, 200), [100, 200, 300, 400])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            div_of_nums("10, 20, 30, 40", 5, 10)
        with self.assertRaises(TypeError):
            div_of_nums([10, 20, 30, 40], "5", 10)
        with self.assertRaises(TypeError):
            div_of_nums([10, 20, 30, 40], 5, "10")
