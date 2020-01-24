import numpy as np
from example import sorting

sorting.COND = 0 
sorting.ASSIGN = 0

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    #odd # array, duplicate values
    x = [1,2,4,0,1]
    y = sorting.bubblesort(x)
    assert [0,1,1,2,4] == y

    #even # array
    x = [1,2,4,0,1,7]
    y = sorting.bubblesort(x)
    assert [0,1,1,2,4,7] == y

    #empty array
    x = []
    y = sorting.bubblesort(x)
    assert [] == y

    #single valued array
    x = [1]
    y = sorting.bubblesort(x)
    assert x == y
    
    # for now, just attempt to call the bubblesort function, should
    # actually check output
def test_insertion():

    x = [1,2,4,0,1]
    y = sorting.insertion_sort(x)
    assert [0,1,1,2,4] == y

    #even # array
    x = [1,2,4,0,1,7]
    y = sorting.insertion_sort(x)
    assert [0,1,1,2,4,7] == y
    #empty array
    x = []
    y = sorting.insertion_sort(x)
    assert y == x

    #single valued array
    x = [1]
    y = sorting.insertion_sort(x)
    assert x == y 

def test_quicksort():

    x = [1,2,4,0,1]
    y = sorting.quick_sort(x)
    assert y == [0,1,1,2,4]

    #even # array
    x = [1,2,4,0,1,7]
    y = sorting.quick_sort(x)
    assert y == [0,1,1,2,4,7]
    #empty array
    x = []
    y = sorting.quick_sort(x)
    assert x == y

    #single valued array
    x = [1]
    y = sorting.quick_sort(x)
    assert y == x
