import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertTrue(check_greater((1, 2, 3), (2, 3, 4)))
        self.assertFalse(check_greater((1, 2, 3), (3, 2, 1)))

    def test_edge_cases(self):
        self.assertTrue(check_greater((1, 1, 1), (1, 1, 1)))
        self.assertFalse(check_greater((1, 1, 1), (1, 1, 0)))

    def test_single_element_tuples(self):
        self.assertTrue(check_greater((1,), (2,)))
        self.assertFalse(check_greater((1,), (0,)))

    def test_empty_tuples(self):
        self.assertTrue(check_greater((), ()))
        self.assertFalse(check_greater((), (1,)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_greater("test", (1, 2, 3))
        with self.assertRaises(TypeError):
            check_greater((1, 2, 3), "test")
