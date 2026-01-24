import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_greater((1, 2, 3), (4, 5, 6)))

    def test_edge_case(self):
        self.assertFalse(check_greater((4, 5, 6), (1, 2, 3)))
        self.assertTrue(check_greater((1, 2, 3), (1, 2, 3)))

    def test_boundary_case(self):
        self.assertFalse(check_greater((1, 2, 3), (1, 2, 4)))
        self.assertTrue(check_greater((1, 2, 3), (1, 2, 2)))

    def test_special_case(self):
        self.assertFalse(check_greater((10, 20, 30), (10, 20, 30)))
        self.assertFalse(check_greater((10, 20, 30), (9, 20, 30)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_greater((1, 2, '3'), (4, 5, 6))
        with self.assertRaises(TypeError):
            check_greater((1, 2, 3), (4, '5', 6))
        with self.assertRaises(TypeError):
            check_greater((1, 2, '3'), (4, '5', 6))
