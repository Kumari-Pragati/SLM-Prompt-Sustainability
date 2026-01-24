import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesnumCorrespondingNum(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(basesnum_coresspondingnum([2, 3, 5], [1, 2, 3]), [2, 9, 125])
        self.assertListEqual(basesnum_coresspondingnum([16, 256], [1, 2]), [16, 65536])

    def test_edge_and_boundary(self):
        self.assertListEqual(basesnum_coresspondingnum([2], [0]), [1])
        self.assertListEqual(basesnum_coresspondingnum([2, 3, 5], [0, 10]), [1, 2, 3125])
        self.assertListEqual(basesnum_coresspondingnum([2, 3, 5], []), [])
        self.assertListEqual(basesnum_coresspondingnum([], [1, 2, 3]), [])

    def test_complex(self):
        self.assertListEqual(basesnum_coresspondingnum([2, 3, 5, 7], [1, 2, 3, 4]), [2, 9, 125, 56849])
        self.assertListEqual(basesnum_coresspondingnum([2, 3, 5, 7], [0, -1]), [1, 1])
