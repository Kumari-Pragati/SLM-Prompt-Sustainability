import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(check_type((1, 2, 3)))
        self.assertTrue(check_type([1, 2, 3]))
        self.assertTrue(check_type((str, str, str)})

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(check_type((1, 2, 3, 4)))
        self.assertTrue(check_type([1, 2, 3, 4]))
        self.assertTrue(check_type((str, str, str, str)))
        self.assertTrue(check_type((1, 1, 1)))
        self.assertTrue(check_type([1, 1, 1]))
        self.assertTrue(check_type((str, str)))
        self.assertTrue(check_type([str, str]))

    def test_invalid_inputs(self):
        self.assertFalse(check_type((1, 2, "str")))
        self.assertFalse(check_type([1, 2, "str"]))
        self.assertFalse(check_type((1, "str", 3)))
        self.assertFalse(check_type([1, "str", 3]))
        self.assertFalse(check_type((1, 2, [1, 2, 3])))
        self.assertFalse(check_type([1, 2, [1, 2, 3]]))
        self.assertFalse(check_type((1, 2, (1, 2, 3))))
        self.assertFalse(check_type([1, 2, (1, 2, 3)]))
