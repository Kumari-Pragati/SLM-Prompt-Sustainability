import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):

    def test_empty_tuple(self):
        result = clear_tuple(())
        self.assertIsInstance(result, tuple)
        self.assertListEqual(list(result), [])

    def test_single_element_tuple(self):
        result = clear_tuple((1,))
        self.assertIsInstance(result, tuple)
        self.assertListEqual(list(result), [])

    def test_multiple_elements_tuple(self):
        result = clear_tuple((1, 2, 3))
        self.assertIsInstance(result, tuple)
        self.assertListEqual(list(result), [])
