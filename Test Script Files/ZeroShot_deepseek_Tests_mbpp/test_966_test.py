import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_remove_empty(self):
        self.assertEqual(remove_empty(((), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',))), ((), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)))
        self.assertEqual(remove_empty(()), ())
        self.assertEqual(remove_empty(('',)), ('',))
        self.assertEqual(remove_empty(('a', 'b')), ('a', 'b'))
        self.assertEqual(remove_empty(('a', 'b', 'c')), ('a', 'b', 'c'))
        self.assertEqual(remove_empty(('d',)), ('d',))
