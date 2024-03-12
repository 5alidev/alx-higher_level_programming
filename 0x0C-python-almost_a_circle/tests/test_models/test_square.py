#!/usr/bin/python3
'''
unittest for Square()
'''
import unittest
import io
from models.base import Base
from models.square import Square
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    '''
    Test cases for Square() class
    '''

    def setUp(self):
        '''
        set up
        '''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''
        clear after each test case
        '''
        pass

    def test_square_type(self):
        '''
        test square type
        '''
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_square_inheritence(self):
        '''
        test if Square inherit from Base()
        '''
        self.assertTrue(issubclass(Square, Base))

    def test_square_constructor(self):
        '''
        test square constructor
        '''
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(e.exception), s)

        s2 = Square(10)
        self.assertEqual(str(type(s2)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(s2, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(s2.__dict__, d)

        with self.assertRaises(TypeError) as e:
            s3 = Square("3")
        err = "width must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(TypeError) as e:
            s3 = Square(3, "3")
        err = "x must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(TypeError) as e:
            s3 = Square(3, 3, "3")
        err = "y must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            s3 = Square(-3)
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            s3 = Square(3, -3)
        err = "x must be >= 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            s3 = Square(3, 3, -3)
        err = "y must be >= 0"
        self.assertEqual(str(e.exception), err)

    def test_square_instantiation(self):
        '''
        test Square() instantition
        '''
        s3 = Square(3, 1, 3)
        d = {'_Rectangle__height': 3, '_Rectangle__width': 3,
             '_Rectangle__x': 1, '_Rectangle__y': 3, 'id': 1}
        self.assertEqual(s3.__dict__, d)

        s1 = Square(99, id=66, y=22, x=44)
        d = {'_Rectangle__height': 99, '_Rectangle__width': 99,
             '_Rectangle__x': 44, '_Rectangle__y': 22, 'id': 66}
        self.assertEqual(s1.__dict__, d)

    def test_square_getter_setters(self):
        '''
        test square getters and setters
        '''
        s1 = Square(10, 4)
        s1.size = 52
        s1.x = 11
        s1.y = 5
        d = {'_Rectangle__height': 52, '_Rectangle__width': 52,
             '_Rectangle__x': 11, '_Rectangle__y': 5, 'id': 1}
        self.assertEqual(s1.__dict__, d)
        self.assertEqual(s1.size, 52)
        self.assertEqual(s1.x, 11)
        self.assertEqual(s1.y, 5)

    def test_square_area(self):
        '''
        test square area() method
        '''
        s1 = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(s1.area(), 25)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, 10)

    def test_square_display(self):
        '''
        test square display method
        '''
        s3 = Square(3)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        s1 = Square(1)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        s1.size = 3
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        s = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)

    def test_square_str(self):
        '''
        test square __str__ method
        '''
        s1 = Square(3, 6)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        s1 = Square(3)
        s = '[Square] (2) 0/0 - 3'
        self.assertEqual(str(s1), s)
        s1 = Square(3, 3)
        s = '[Square] (3) 3/0 - 3'
        self.assertEqual(str(s1), s)
        s1 = Square(1, 2, 3, 4)
        s = '[Square] (4) 2/3 - 1'
        self.assertEqual(str(s1), s)

    def test_square_update(self):
        '''
        test square update() method
        '''
        s1 = Square(3, 6)
        with self.assertRaises(TypeError) as e:
            Square.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = s1.__dict__.copy()
        s1.update()
        self.assertEqual(s1.__dict__, d)

        s1.update(10)
        d["id"] = 10
        self.assertEqual(s1.__dict__, d)

        s1.update(10, 7)
        d["_Rectangle__height"] = 7
        d["_Rectangle__width"] = 7
        self.assertEqual(s1.__dict__, d)

    def test_square_update_kwargs(self):
        '''
        test square update with **kwargs
        '''
        s1 = Square(3, 7)
        d = s1.__dict__.copy()

        s1.update(id=10)
        d["id"] = 10
        self.assertEqual(s1.__dict__, d)

        s1.update(size=33)
        d["_Rectangle__height"] = 33
        d["_Rectangle__width"] = 33
        self.assertEqual(s1.__dict__, d)

        s1.update(y=33)
        d["_Rectangle__y"] = 33
        self.assertEqual(s1.__dict__, d)
        s1.update(x=44)
        d["_Rectangle__x"] = 44
        self.assertEqual(s1.__dict__, d)

    def test_square_to_dictionary(self):
        '''
        test square to_dictionary() method
        '''
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        s1 = Square(5, 7, 9, 11)
        d = {'x': 7, 'y': 9, 'size': 5, 'id': 11}
        self.assertEqual(s1.to_dictionary(), d)

        s2 = Square(11, 5, 2)
        s2_dictionary = s2.to_dictionary()
        s3 = Square(3, 3)
        s3.update(**s2_dictionary)
        self.assertEqual(str(s2), str(s3))
        self.assertNotEqual(s2, s3)


if __name__ == "__main__":
    unittest.main()
