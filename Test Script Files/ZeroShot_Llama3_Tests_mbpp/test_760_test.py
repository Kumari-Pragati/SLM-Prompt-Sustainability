import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):

    def test_unique_element(self):
        self.assertEqual(unique_Element([1],1), 'YES')
        self.assertEqual(unique_Element([1,1],1), 'NO')
        self.assertEqual(unique_Element([1,2,3],3), 'YES')
        self.assertEqual(unique_Element([1,2,2,3],3), 'NO')
        self.assertEqual(unique_Element([],0), 'YES')
        self.assertEqual(unique_Element([1,1,1,1],1), 'NO')
        self.assertEqual(unique_Element([1,2,3,4,5],5), 'YES')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            unique_Element(None,1)
        with self.assertRaises(TypeError):
            unique_Element([1,2,3],None)
        with self.assertRaises(TypeError):
            unique_Element([1,2,3],0)
