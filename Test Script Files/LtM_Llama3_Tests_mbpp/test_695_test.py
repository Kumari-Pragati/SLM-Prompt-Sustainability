import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertTrue(check_greater((1, 2), (1, 2)))
        self.assertFalse(check_greater((1, 2), (2, 1)))

    def test_empty_inputs(self):
        self.assertFalse(check_greater((), ()))
        self.assertFalse(check_greater((), (1,)))
        self.assertFalse(check_greater((1,), ()))

    def test_single_element_tuples(self):
        self.assertTrue(check_greater((1,), (1,)))
        self.assertFalse(check_greater((1,), (2,)))

    def test_max_and_min_values(self):
        self.assertTrue(check_greater((2**31 - 1, 2**31 - 1), (2**31 - 1, 2**31 - 1)))
        self.assertFalse(check_greater((2**31 - 1, 2**31 - 1), (2**31, 2**31)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_greater('test', (1, 2))
        with self.assertRaises(TypeError):
            check_greater((1, 2), 'test')
