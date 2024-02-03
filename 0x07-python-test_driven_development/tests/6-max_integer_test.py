#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''
    class who contains test cases for max_integer function
    '''

    def test_positive_int(self):
        """
        test by positive integers
        """
        testList1 = [0, 6, 2, 1]
        testList2 = [2, 3, 4, 8]
        testList3 = [9, 7, 2, 1, 5]

        self.assertEqual(max_integer(testList1), 6)
        self.assertEqual(max_integer(testList2), 8)
        self.assertEqual(max_integer(testList3), 9)

    def test_negative_int(self):
        '''
        test by negative numbers
        '''
        testList1 = [-2, -6, -5, -11]
        testList2 = [-2, -3, -4, -8]
        testList3 = [-9, -7, -2, -1, -5]

        self.assertEqual(max_integer(testList1), -2)
        self.assertEqual(max_integer(testList2), -2)
        self.assertEqual(max_integer(testList3), -1)

    def test_empty_list(self):
        '''
        test if list is empty
        '''
        testListEmpty = []
        self.assertIsNone(max_integer(testListEmpty), None)

    def test_none_arg(self):
        '''
        test for None as arg
        '''
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_one_arg(self):
        '''
        test for one arg
        '''
        testList = [26]
        self.assertIsNone(max_integer(testList), 26)

    def test_none_list(self):
        '''
        test None as a single element in list
        '''
        testList = [None]
        self.assertIsNone(max_integer(testList), None)


if __name__ == '__main__':
    unittest.main()
