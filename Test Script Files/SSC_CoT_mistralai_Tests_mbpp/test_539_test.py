import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesnumCorrespondingNum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 5], [2, 3]), [4, 27, 125])
        self.assertEqual(basesnum_coresspondingnum([10, 16], [2, 3]), [100, 4096])

    def test_edge_and_boundary_cases(self):
        self.assertEqual(basesnum_coresspondingnum([2], [0]), [1])
        self.assertEqual(basesnum_coresspondingnum([2], [1]), [2])
        self.assertEqual(basesnum_coresspondingnum([2], [2]), [4])
        self.assertEqual(basesnum_coresspondingnum([2], [3]), [8])
        self.assertEqual(basesnum_coresspondingnum([2], [4]), [16])

        self.assertEqual(basesnum_coresspondingnum([2, 3, 5], [0]), [1, 1, 1])
        self.assertEqual(basesnum_coresspondingnum([2, 3, 5], [1]), [2, 3, 5])
        self.assertEqual(basesnum_coresspondingnum([2, 3, 5], [2]), [4, 9, 25])
        self.assertEqual(basesnum_coresspondingnum([2, 3, 5], [3]), [8, 27, 125])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, basesnum_coresspondingnum, 'string', [1])
        self.assertRaises(TypeError, basesnum_coresspondingnum, [1], 'string')
        self.assertRaises(TypeError, basesnum_coresspondingnum, [1, 2], [1, 'string'])
