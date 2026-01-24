import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):
    def test_valid_input(self):
        self.assertTrue(check_valid((True, True, True)))
        self.assertTrue(check_valid((True, False, True)))
        self.assertTrue(check_valid((True, True, False)))
        self.assertTrue(check_valid((True, True, True)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_valid('test')
        with self.assertRaises(TypeError):
            check_valid([1, 2, 3])
        with self.assertRaises(TypeError):
            check_valid({'a': 1, 'b': 2})

    def test_edge_case(self):
        self.assertFalse(check_valid((False, False, False)))
        self.assertFalse(check_valid((False, True, False)))
        self.assertFalse(check_valid((False, False, True)))
        self.assertFalse(check_valid((False, False, False)))

    def test_empty_input(self):
        self.assertFalse(check_valid(()))
