import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_num_keith(14))
        self.assertTrue(is_num_keith(407))
        self.assertTrue(is_num_keith(1974))

    def test_edge_cases(self):
        self.assertFalse(is_num_keith(0))
        self.assertFalse(is_num_keith(1))
        self.assertFalse(is_num_keith(10))
        self.assertFalse(is_num_keith(100))

    def test_boundary_cases(self):
        self.assertTrue(is_num_keith(179))
        self.assertFalse(is_num_keith(180))
        self.assertFalse(is_num_keith(181))
        self.assertFalse(is_num_keith(182))
        self.assertFalse(is_num_keith(183))
        self.assertFalse(is_num_keith(184))
        self.assertFalse(is_num_keith(185))
        self.assertFalse(is_num_keith(186))
        self.assertFalse(is_num_keith(187))
        self.assertFalse(is_num_keith(188))
        self.assertFalse(is_num_keith(189))
        self.assertFalse(is_num_keith(190))
        self.assertFalse(is_num_keith(191))
        self.assertFalse(is_num_keith(192))
        self.assertFalse(is_num_keith(193))
        self.assertFalse(is_num_keith(194))
        self.assertFalse(is_num_keith(195))
        self.assertFalse(is_num_keith(196))
        self.assertFalse(is_num_keith(197))
        self.assertFalse(is_num_keith(198))
        self.assertFalse(is_num_keith(199))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_num_keith("14")
        with self.assertRaises(TypeError):
            is_num_keith(14.5)
        with self.assertRaises(TypeError):
            is_num_keith([])
        with self.assertRaises(TypeError):
            is_num_keith({})
