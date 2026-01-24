import unittest
from mbpp_847_code import deepcopy
from 847_code import lcopy

class TestLcopy(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(lcopy([]), [])

    def test_single_element_list(self):
        self.assertEqual(lcopy([1]), [1])

    def test_list_with_multiple_elements(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])

    def test_list_with_different_types(self):
        self.assertEqual(lcopy([1, "a", 3.14]), [1, "a", 3.14])

    def test_list_with_nested_lists(self):
        self.assertEqual(lcopy([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_list_with_mutable_objects(self):
        class TestObject:
            def __init__(self, value):
                self.value = value

        obj1 = TestObject(1)
        obj2 = TestObject(2)
        original_list = [obj1, obj2]
        copied_list = lcopy(original_list)
        copied_list[0].value = 3
        self.assertNotEqual(copied_list[0].value, original_list[0].value)
