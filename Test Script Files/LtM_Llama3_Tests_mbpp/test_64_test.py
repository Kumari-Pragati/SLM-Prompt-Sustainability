import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(subject_marks([]), [])

    def test_single_element_input(self):
        self.assertEqual(subject_marks([('English', 88)]), [('English', 88)])

    def test_multiple_elements_input(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), 
                         [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])

    def test_descending_order(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), 
                         [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)])

    def test_ascending_order(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)], reverse=True), 
                         [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)])

    def test_duplicates(self):
        self.assertEqual(subject_marks([('English', 88), ('English', 88), ('Science', 90), ('Maths', 97)]), 
                         [('English', 88), ('English', 88), ('Maths', 97), ('Science', 90)])
