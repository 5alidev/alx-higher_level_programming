#!/usr/bin/python3
'''
unittest module for base class
'''
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    '''
    Test class to test Base class
    '''

    def setUp(self):
        '''
        instantiates class
        '''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''
        cleans up after each test_method
        '''
        pass

    def test_constructor(self):
        '''
        test Base constructor
        '''

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_nb_objects_exist(self):
        '''
        test if Base has a private nb_objects attribute
        '''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_nb_objects_initialized(self):
        '''
        test if nb_objects initializes to zero
        '''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instantiation(self):
        '''
        test Base() instantiation
        '''
        b1 = Base()
        self.assertEqual(str(type(b1)), "<class 'models.base.Base'>")
        self.assertEqual(b1.__dict__, {"id": 1})
        self.assertEqual(b1.id, 1)

    def test_consecutive_ids(self):
        '''
        test with consecutive ids
        '''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_more_constructor(self):
        '''
        test constructoc signature
        '''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        err = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

    def test_nb_objects_eq_id(self):
        '''
        test if nb_objects is sync to id
        '''
        b1 = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b1.id)

    def test_more_nb_objects_eq_id(self):
        '''
        more tests to check if nb_objects is sync to id
        '''
        b1 = Base()
        b1 = Base('Foo')
        b1 = Base(98)
        b1 = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b1.id)

    def test_to_json_string(self):
        '''
        test to_json_string() method
        '''
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        m = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), m)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'x': 12, 'y': 20, 'width': 2024,
             'id': 2025, 'height': 2030}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))
        d = [{'x': 10, 'y': 11, 'width': 12, 'id': 13, 'height': 14}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))
        d = [{"something": 20202020}]
        self.assertEqual(Base.to_json_string(d), '[{"something": 20202020}]')

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([r1_dictionary])
        r1_dictionary = str([r1_dictionary])
        r1_dictionary = r1_dictionary.replace("'", '"')
        self.assertEqual(r1_dictionary, json_dictionary)

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([s1_dictionary])
        s1_dictionary = str([s1_dictionary])
        s1_dictionary = s1_dictionary.replace("'", '"')
        self.assertEqual(s1_dictionary, json_dictionary)

    def test_from_json_string(self):
        '''
        test from_json_string() method
        '''
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])

        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"something": 20252030}, {"test": 1234}, {"Foo": 98}]
        s = '[{"something": 20252030}, {"test": 1234}, {"Foo": 98}]'
        self.assertEqual(Base.from_json_string(s), d)

    def test_save_to_file(self):
        '''
        test save_to_file() method
        '''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_create(self):
        '''
        test create() method
        '''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        '''
        test load_from_file() method
        '''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_input[0]), id(list_out[0]))
        self.assertEqual(str(list_input[0]), str(list_out[0]))
        self.assertNotEqual(id(list_input[1]), id(list_out[1]))
        self.assertEqual(str(list_input[1]), str(list_out[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_s_input = [s1, s2]
        Square.save_to_file(list_s_input)
        list_s_output = Square.load_from_file()
        self.assertNotEqual(id(list_s_input[0]), id(list_s_output[0]))
        self.assertEqual(str(list_s_input[0]), str(list_s_output[0]))


if __name__ == "__main__":
    unittest.main()
