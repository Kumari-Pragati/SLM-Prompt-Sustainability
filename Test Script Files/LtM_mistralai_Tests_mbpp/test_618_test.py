import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(div_list([1, 2, 3], [1, 2, 3]), [1.0, 1.0, 1.0])
        self.assertListEqual(div_list([4, 4, 4], [2, 2, 2]), [2.0, 2.0, 2.0])

    def test_edge_cases(self):
        self.assertListEqual(div_list([0, 0], [1, 2]), [0.0, float('inf')])
        self.assertListEqual(div_list([1, 2], [0, 0]), [float('inf'), 0.0])
        self.assertRaises(ZeroDivisionError, div_list, [1, 0], [1, 2])

    def test_boundary_conditions(self):
        self.assertListEqual(div_list([minint], [1]), [minint])
        self.assertListEqual(div_list([1], maxint), [0])
        self.assertListEqual(div_list([minint], maxint), [0])
        self.assertListEqual(div_list([maxint], [minint]), [0])
