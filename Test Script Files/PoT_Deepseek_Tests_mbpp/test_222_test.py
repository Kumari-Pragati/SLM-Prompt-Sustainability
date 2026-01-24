import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_type((1, 2, 3)))
        self.assertTrue(check_type(('a', 'b', 'c')))

    def test_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_type((1,)))
        self.assertTrue(check_type(('a',)))

    def test_different_types(self):
        self.assertFalse(check_type((1, 'a')))
        self.assertFalse(check_type((1, 2.0)))

    def test_mixed_types(self):
        self.assertFalse(check_type((1, 'a', 2.0)))

    def test_tuple_with_none(self):
        self.assertFalse(check_type((1, None)))

    def test_tuple_with_subclass(self):
        class SubClass(int):
            pass
        self.assertTrue(check_type((SubClass(1), SubClass(2))))

    def test_tuple_with_subclass_different_type(self):
        class SubClass(int):
            pass
        self.assertFalse(check_type((SubClass(1), 'a')))
