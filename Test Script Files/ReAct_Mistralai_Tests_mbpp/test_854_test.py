import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(raw_heap([]), [])

    def test_single_element(self):
        self.assertEqual(raw_heap([1]), [1])

    def test_multiple_elements(self):
        self.assertEqual(raw_heap([3, 1, 5, 2, 4]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(raw_heap([-3, -1, 0, 2, -4]), [-3, -1, 0, 2, -4])

    def test_floats(self):
        self.assertEqual(raw_heap([1.5, 2.7, 3.3]), [1.5, 2.7, 3.3])

    def test_duplicates(self):
        self.assertEqual(raw_heap([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_list_with_tuple(self):
        self.assertEqual(raw_heap([(1, 'a'), (2, 'b'), (3, 'c')]), [(1, 'a'), (2, 'b'), (3, 'c')])

    def test_list_with_custom_objects(class _CustomObject:
        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            return self.value < other.value

    custom_objs = [_CustomObject(3), _CustomObject(1), _CustomObject(2)]
    self.assertEqual(raw_heap(custom_objs), [_CustomObject(1), _CustomObject(2), _CustomObject(3)])
