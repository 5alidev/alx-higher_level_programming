#!/usr/bin/python3
'''
unittest for Rectangle class
'''
import unittest
import io
from models.base import Base
from models.rectangle import Rectangle
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    '''
    test the Rectangle class
    '''

    def setUp(self):
        '''
        set up
        '''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''
        clean after each test case method
        '''
        pass

    def test_rectangle_inheritence(self):
        '''
        test if Rectangle ()class inherits from Base()
        '''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rectangle_type(self):
        '''
        test rectangle class type
        '''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_rectangle_constructor(self):
        '''
        test rectangle constructor
        '''
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 4, 6, 8, 10, 12)
        s = "__init__() takes from 3 to 6 positional arguments but 7 were \
given"
        self.assertEqual(str(e.exception), s)

        '''constructor with one arg'''
        with self.assertRaises(TypeError) as e:
            r2 = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_rectangle_instance(self):
        '''
        test rectangle class instanciation
        '''
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(str(type(r1)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r2, Base))
        d = {'_Rectangle__height': 2, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r1.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r3 = Rectangle(2, "2")
        err = "height must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(TypeError) as e:
            r3 = Rectangle("2", 2)
        err = "width must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(TypeError) as e:
            r3 = Rectangle(1, 2, "3")
        err = "x must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(TypeError) as e:
            r3 = Rectangle(1, 2, 3, "4")
        err = "y must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r3 = Rectangle(-2, 2)
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r3 = Rectangle(2, -2)
        err = "height must be > 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r3 = Rectangle(1, 2, -3)
        err = "x must be >= 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r3 = Rectangle(1, 2, 3, -4)
        err = "y must be >= 0"
        self.assertEqual(str(e.exception), err)

    def test_rectangle_id(self):
        '''
        test inheritence of id attribute
        '''
        Base._Base__nb_objects = 98
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.id, 99)

    def test_getters_and_setter(self):
        '''
        test getters and setters
        '''
        r1 = Rectangle(2, 1)
        r1.width = 10
        r1.height = 20
        r1.x = 30
        r1.y = 40
        d = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 30, '_Rectangle__y': 40, 'id': 1}
        self.assertEqual(r1.__dict__, d)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 30)
        self.assertEqual(r1.y, 40)

    def test_rectangle_area(self):
        '''
        test area() method
        '''
        r1 = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        r2 = Rectangle(5, 6)
        self.assertEqual(r2.area(), 30)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_rectangle_display(self):
        '''
        test rectangle display() method
        '''
        r1 = Rectangle(8, 9)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        r2 = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r2.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r2.width = 3
        r2.height = 5
        f = io.StringIO()
        with redirect_stdout(f):
            r2.display()
        s = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"

        def test_rectangle_str(self):
            '''
            test rectangle __str__
            '''
            r1 = Rectangle(5, 2)
            with self.assertRaises(TypeError) as e:
                Rectangle.__str__()
            s = "__str__() missing 1 required positional argument: 'self'"
            self.assertEqual(str(e.exception), s)

            r2 = Rectangle(5, 2)
            s = '[Rectangle] (1) 0/0 - 5/2'
            self.assertEqual(str(r2), s)

            r3 = Rectangle(4, 6, 2, 1, 12)
            s = '[Rectangle] (12) 2/1 - 4/6'
            self.assertEqual(str(r3), s)

            r4 = Rectangle(5, 5, 1)
            s = '[Rectangle] (1) 1/0 - 5/5'
            self.assertEqual(str(r4), s)

        def test_rectangle_update(self):
            '''
            test rectangle update() method
            '''
            r1 = Rectangle(5, 2)
            with self.assertRaises(TypeError) as e:
                Rectangle.update()
            s = "update() missing 1 required positional argument: 'self'"
            self.assertEqual(str(e.exception), s)

            d = r1.__dict__.copy()
            r1.update()
            self.assertEqual(r1.__dict__, d)

            r1.update(10)
            d["id"] = 10
            self.assertEqual(r1.__dict__, d)

            r1.update(10, 5)
            d["_Rectangle__width"] = 5
            self.assertEqual(r1.__dict__, d)

            r1.update(10, 5, 17)
            d["_Rectangle__height"] = 17
            self.assertEqual(r1.__dict__, d)

            r1.update(10, 5, 17, 20)
            d["_Rectangle__x"] = 20
            self.assertEqual(r1.__dict__, d)

        def test_rectangle_update_kwargs(self):
            '''
            test update() with **kwargs
            '''
            r1 = Rectangle(5, 2)
            d = r1.__dict__.copy()

            r1.update(id=10)
            d["id"] = 10
            self.assertEqual(r1.__dict__, d)

            r1.update(height=12)
            d["_Rectangle__height"] = 12
            self.assertEqual(r1.__dict__, d)

        def test_rectangle_to_dictionary(self):
            '''
            test to_dictionary() method
            '''
            with self.assertRaises(TypeError) as e:
                Rectangle.to_dictionary()
            s = "to_dictionary() missing 1 required \
positional argument: 'self'"
            self.assertEqual(str(e.exception), s)

            r1 = Rectangle(1, 2)
            d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
            self.assertEqual(r1.to_dictionary(), d)

            r2 = Rectangle(1, 2, 3, 4, 5)
            d = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
            self.assertEqual(r2.to_dictionary(), d)


if __name__ == "__main__":
    unittest.main()
