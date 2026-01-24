import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):

    def test_unique_element(self):
        self.assertEqual(unique_Element([1, 2, 3, 4, 5], 5), 'YES')
        self.assertEqual(unique_Element([1, 1, 1, 1, 1], 5), 'YES')
        self.assertEqual(unique_Element([1, 2, 2, 3, 4], 5), 'NO')
        self.assertEqual(unique_Element([], 0), 'YES')
        self.assertEqual(unique_Element([1], 1), 'YES')
        self.assertEqual(unique_Element([1, 2], 2), 'NO')
