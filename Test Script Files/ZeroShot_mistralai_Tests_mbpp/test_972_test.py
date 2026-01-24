import unittest
from972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_concatenate_nested(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))
        self.assertEqual(concatenate_nested(('a', 'b'), ('c', 'd')), ('a', 'b', 'c', 'd'))
        self.assertEqual(concatenate_nested([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(concatenate_nested([('a', 'b'), ('c', 'd')], [('e', 'f'), ('g', 'h')]), [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h')])
