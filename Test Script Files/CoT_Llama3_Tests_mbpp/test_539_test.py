import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesnumCoresspondingnum(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [1, 2, 3]), [2, 9, 16])

    def test_edge_cases(self):
        self.assertEqual(basesnum_coresspondingnum([2], [1]), [2])
        self.assertEqual(basesnum_coresspondingnum([2, 3], []), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum('abc', [1, 2, 3])
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum([2, 3], 'abc')

    def test_boundary_conditions(self):
        self.assertEqual(basesnum_coresspondingnum([2], [0]), [1])
        self.assertEqual(basesnum_coresspondingnum([2], [1]), [2])
