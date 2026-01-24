import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertTrue(check_greater((1, 2, 3), (4, 5, 6)))
        self.assertFalse(check_greater((4, 5, 6), (1, 2, 3)))
        self.assertFalse(check_greater((1, 2, 3), (1, 2, 3)))

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertTrue(check_greater((), ()))
        self.assertFalse(check_greater((1,), ()))
        self.assertFalse(check_greater((), (1,)))
        self.assertFalse(check_greater((1, 2, 3), (1, 2)))
        self.assertFalse(check_greater((1, 2), (1, 2, 3)))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertFalse(check_greater((10, 20, 30), (10, 20, 30)))
        self.assertFalse(check_greater((10, 20, 30), (9, 20, 30)))
        self.assertFalse(check_greater((10, 20, 30), (10, 19, 30)))
        self.assertFalse(check_greater((10, 20, 30), (10, 20, 29)))
