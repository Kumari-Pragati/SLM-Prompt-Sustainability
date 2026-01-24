import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesNumCorrespondingNum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [0, 1, 2]), [1, 3, 256])

    def test_edge_conditions(self):
        self.assertEqual(basesnum_coresspondingnum([], []), [])
        self.assertEqual(basesnum_coresspondingnum([2], [0]), [1])
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [0, 0, 0]), [1, 1, 1])

    def test_boundary_conditions(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [1, 2, 3]), [2, 9, 64])
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [3, 2, 1]), [8, 9, 64])

    def test_complex_cases(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [2, 3, 4]), [4, 27, 256])
        self.assertEqual(basesnum_coresspondingnum([5, 6, 7], [1, 2, 3]), [5, 36, 343])
