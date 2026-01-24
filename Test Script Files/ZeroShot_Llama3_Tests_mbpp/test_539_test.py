import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesNumCorrespondingNum(unittest.TestCase):

    def test_basesnum_coresspondingnum(self):
        self.assertEqual(basesnum_coresspondingnum([2,3,4], [0,1,2]), [1, 3, 16])
        self.assertEqual(basesnum_coresspondingnum([10,10,10], [0,1,2]), [1, 1, 1])
        self.assertEqual(basesnum_coresspondingnum([2,3,4], [1,0,2]), [3, 1, 16])
        self.assertEqual(basesnum_coresspondingnum([2,3,4], [2,1,0]), [4, 3, 1])
        self.assertEqual(basesnum_coresspondingnum([2,3,4], [0,1,2,3]), [1, 3, 16, 64])

    def test_basesnum_coresspondingnum_empty_list(self):
        self.assertEqual(basesnum_coresspondingnum([], [0,1,2]), [])

    def test_basesnum_coresspondingnum_empty_index(self):
        self.assertEqual(basesnum_coresspondingnum([2,3,4], []), [])

    def test_basesnum_coresspondingnum_invalid_input(self):
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum('a', [0,1,2])
