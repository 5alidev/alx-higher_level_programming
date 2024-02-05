#!/usr/bin/python3
'''MyList class that inherits from list'''


class MyList(list):
    '''
    MyList class that inherites from the list object

    Args:
        list: list object
    '''

    def print_sorted(self):
        '''
            print the list in ascending order
        '''

        print(sorted(self))
