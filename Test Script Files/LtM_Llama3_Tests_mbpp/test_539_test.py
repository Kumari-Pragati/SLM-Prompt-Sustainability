import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesnumCoresspondingnum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3], [1, 2]), [2, 3])
        self.assertEqual(basesnum_coresspondingnum([2, 3], [1, 3]), [2, 4])
        self.assertEqual(basesnum_coresspondingnum([2, 3], [2, 3]), [4, 9])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3], []), [])
        self.assertEqual(basesnum_coresspondingnum([], [1, 2]), [])
        self.assertEqual(basesnum_coresspondingnum([2, 3], [1, 1]), [2, 2])
        self.assertEqual(basesnum_coresspondingnum([2, 3], [1, 4]), [2, 81])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum('a', [1, 2])
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum([2, 3], 'a')
