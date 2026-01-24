import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_simple_non_empty_tuple(self):
        self.assertListEqual(remove_empty((1, 2, 3)), (1, 2, 3))
        self.assertListEqual(remove_empty(('a', 'b', 'c')), ('a', 'b', 'c'))

    def test_empty_tuple(self):
        self.assertListEqual(remove_empty(()), ())
        self.assertListEqual(remove_empty(()), ())

    def test_single_empty_element_tuple(self):
        self.assertListEqual(remove_empty(('', 'a')), ('a',))
        self.assertListEqual(remove_empty((None, 1, 2)), (1, 2))

    def test_multiple_empty_elements_tuple(self):
        self.assertListEqual(remove_empty(('', '', 'a')), ('a',))
        self.assertListEqual(remove_empty((None, None, 1)), (1,))

    def test_mixed_empty_and_non_empty_tuple(self):
        self.assertListEqual(remove_empty(('', 'a', 'b')), ('a', 'b'))
        self.assertListEqual(remove_empty((None, 'a', 1)), ('a', 1))
