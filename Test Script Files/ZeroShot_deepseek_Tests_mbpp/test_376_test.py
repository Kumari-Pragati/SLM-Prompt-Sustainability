import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):

    def test_remove_replica(self):
        self.assertEqual(remove_replica(('a', 'b', 'c', 'a')), ('a', 'b', 'c', 'MSP'))
        self.assertEqual(remove_replica(('1', '2', '3', '2')), ('1', '2', '3', 'MSP'))
        self.assertEqual(remove_replica(('apple', 'banana', 'cherry', 'apple')), ('apple', 'banana', 'cherry', 'MSP'))
        self.assertEqual(remove_replica(('a', 'a', 'a', 'a')), ('a', 'MSP', 'MSP', 'MSP'))
        self.assertEqual(remove_replica(('1', '1', '1', '1')), ('1', 'MSP', 'MSP', 'MSP'))
        self.assertEqual(remove_replica(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a')), ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'MSP'))
