import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_greater((1, 2, 3), (4, 5, 6)))

    def test_edge_condition(self):
        self.assertFalse(check_greater((1, 2, 3), (1, 2, 3)))

    def test_boundary_condition(self):
        self.assertTrue(check_greater((1, 2, 3), (4, 5, 7)))
        self.assertFalse(check_greater((4, 5, 6), (1, 2, 3)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_greater((1, 2, '3'), (4, 5, 6))
