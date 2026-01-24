import unittest
from mbpp_376_code import Tuple

from 376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_replica(tuple()), ('MSP',))

    def test_single_element(self):
        self.assertEqual(remove_replica((1,)), (1,))

    def test_duplicate_elements(self):
        self.assertEqual(remove_replica((1, 1, 2, 2, 3)), (1, 2, 3, 'MSP', 'MSP'))

    def test_unique_elements(self):
        self.assertEqual(remove_replica((1, 2, 3)), (1, 2, 3))
