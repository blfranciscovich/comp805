"""
Bridget Franciscovich
UNHM COMP705/805 Lab 2
An Introduction to Python
Feb 6, 2018

The purpose of this file is to test the functions declared in
lab2.py. This file does not use pythons unit test framework.
This is because this file is intended to by used as a learning
tool as well.

"""
import lab2

def run_squared_nums():
    """
    Demo many uses of the function squared_nums()
    Test Cases:
    [1, 2, 3], [], [-1, -2, -3], [1, 0]
    
    Expected Results:
    [1, 4, 9], [], [1, 4, 9], [1, 0]
    """
    tc = [1, 2, 3]
    res = lab2.squared_nums(tc)
    print('squared_nums({}) --> {}'.format(tc, res))

    tc = []
    res = lab2.squared_nums(tc)
    print('squared_nums({}) --> {}'.format(tc, res))

    tc = [-1, -2, -3]
    res = lab2.squared_nums(tc)
    print('squared_nums({}) --> {}'.format(tc, res))

    tc = [1, 0]
    res = lab2.squared_nums(tc)
    print('squared_nums({}) --> {}'.format(tc, res))

def run_check_title():
    """
    Demo many uses of the function check_title()
    Test Cases:
    ['Hello World', 'Hello_world', 'Title'], ['Hello_World', 'A great 3 Days', 'hello World'], [‘10, 11, 12’]
    
    Expected Results:
    ['Hello World',  'Title'], ['Hello_World'], []
    
    """
    tc = ['Hello World', 'Hello_world', 'Title']
    res = lab2.check_title(tc)
    print('check_title({}) --> {}'.format(tc, res))

    tc = ['Hello_World', 'A great 3 Days', 'hello World']
    res = lab2.check_title(tc)
    print('check_title({}) --> {}'.format(tc, res))   

    tc = ["10, 11, 12"]
    res = lab2.check_title(tc)
    print('check_title({}) --> {}'.format(tc, res)) 

def run_restock_inventory():
    """
    Demo many uses of the function check_title()
    Test Cases:
    {'pencil':10, 'pen':8, 'paper':7}, {'pencil':0, 'pen':-3, 'paper':-11}, 
    {'pencil':0.5, 'pen':-3.2, 'paper':11.0}
    
    Expected Results:
    {'pencil':20, 'pen':18, 'paper':17}, 
    {'pencil':10, 'pen':7, 'paper':-1}, 
    {'pencil':10.5, 'pen':6.8, 'paper':21.0}
    
    """

    tc = {'pencil':10, 'pen':8, 'paper':7}
    res = lab2.restock_inventory(tc)
    print('restock_inventory({}) --> {}'.format(tc, res))

    tc = {'pencil':0, 'pen':-3, 'paper':-11}
    res = lab2.restock_inventory(tc)
    print('restock_inventory({}) --> {}'.format(tc, res)) 

    tc = {'pencil':0.5, 'pen':-3.2, 'paper':11.0}
    res = lab2.restock_inventory(tc)
    print('restock_inventory({}) --> {}'.format(tc, res)) 

def run_filter_0_items():
    """
    Demo many uses of the function check_title()
    Test Cases:
    {'pencil':10, 'pen':8, 'paper':7}, {'pencil':0, 'pen':-3, 'paper':-11}, 
    {'pencil':0.5, 'pen':-3.2, 'paper':0.0}

    Expected Results:
    {'pen':8, 'paper':7, 'pencil':10}, {'pen':-3, 'paper':-11}, 
    {'pen':-3.2, 'pencil':0.5}
    
    """

    tc = {'pencil':10, 'pen':8, 'paper':7}
    res = lab2.filter_0_items(tc)
    print('filter_0_items({}) --> {}'.format(tc, res))
    
    tc = {'pencil':0, 'pen':-3, 'paper':-11}
    res = lab2.filter_0_items(tc)
    print('filter_0_items({}) --> {}'.format(tc, res))

    tc = {'pencil':0.5, 'pen':-3.2, 'paper':0.0}
    res = lab2.filter_0_items(tc)
    print('filter_0_items({}) --> {}'.format(tc, res))

def run_average_grades():
    """
    Demo many uses of the function average_grades()
    
    Test Cases:
    {'Michael' :[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}, 
    {'Michael' :[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0], 'Josh':[99 + 1 * -2, 40/.5]}, 
    {'Michael' :[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0],'Josh':[99 + 1 * -2, 40/.5]}

    Expected Results:
    {'Josh' : 87.0, 'Daniel': 79.0, 'Michael': 89.0},
    {'Josh' : 88.5, 'Daniel': 52.6625, 'Michael': 94.0},
    {'Josh' : -100.0, 'Daniel': 90.0, 'Michael': 78.0}

    """

    tc = {'Michael':[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}
    res = lab2.average_grades(tc)
    print('average_grades({}) --> {}'.format(tc, res))

    tc = {'Michael':[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0], 'Josh':[99 + 1 * -2, 40/.5]}
    res = lab2.average_grades(tc)
    print('average_grades({}) --> {}'.format(tc, res)) 

    tc = {'Michael':[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0], 'Josh':[99 + 1 * -2, 40/.5]}
    res = lab2.average_grades(tc)
    print('average_grades({}) --> {}'.format(tc, res))

def main( ):
    '''
    Calls the testing functions defining in this module
    '''
    run_squared_nums( )
    print( )

    run_check_title( )
    print( )

    run_restock_inventory( )
    print( )

    run_filter_0_items( )
    print( )

    run_average_grades( )
    print( )

if __name__ == "__main__":
    main( )