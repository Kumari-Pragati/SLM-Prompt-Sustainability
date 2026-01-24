import unittest
from mbpp_64_code import range
from six.moves import map

from64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):

    def test_sorted_marks(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)])
        self.assertEqual(subject_marks([('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]), [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)])
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] * 100), [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)] * 100)

    def test_equal_marks(self):
        self.assertEqual(subject_marks([('English', 88), ('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), [('English', 88), ('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] )
        self.assertEqual(subject_marks([('English', 88), ('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] * 100), [('English', 88), ('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] * 100)

    def test_empty_list(self):
        self.assertEqual(subject_marks([]), [])

    def test_single_subject(self):
        self.assertEqual(subject_marks([('English', 88)]), [('English', 88)])

    def test_subject_without_marks(self):
        self.assertRaises(TypeError, subject_marks, [('English',)])

    def test_invalid_marks(self):
        self.assertRaises(TypeError, subject_marks, [('English', 'invalid_marks')])
