import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesnumCoresspondingnum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [1, 2, 3]), [2, 9, 16])

    def test_edge_cases(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3], [1, 2]), [2, 9])
        self.assertEqual(basesnum_coresspondingnum([2], [1]), [2])

    def test_boundary_cases(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [1, 2, 4]), [2, 9, 256])
        self.assertEqual(basesnum_coresspondingnum([2, 3], [1, 3]), [2, 27])

    def test_special_cases(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3], [0, 1]), [1, 2])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum('abc', [1, 2, 3])
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum([1, 2, 3], 'abc')
