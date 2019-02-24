# Function to find the i'th biggest element in a list
import random

def ith_elem(arr, i):
    """
    Given an array "arr" and the index "i", return the i'th biggest element
    in the array. i is 0 indexed.
    """
    def find_ith_elem_recursive(arr, i, low, high):
        """
        Given an array "arr" and the index "i", return the i'th biggest element
        in the range arr[low:high]
        """
        if low+1 == high:
            if i >= high - low:
                raise Exception("Array is %s, index is %s,"
                                "Low is %s, High is %s. Something went Wrong"
                       %(arr, i, low, high))
            return arr[low]
        elem = arr[low]
        tracker = low
        for idx in range(low+1, high):
            if arr[idx] < elem:
                tracker +=1
                arr[tracker], arr[idx] = arr[idx], arr[tracker]
        arr[tracker], arr[low] =  arr[low], arr[tracker]
        if tracker == i+low:
            return arr[tracker]
        elif tracker > i+low:
           return find_ith_elem_recursive(arr, i, low, tracker)
        else:
            return find_ith_elem_recursive(arr, i-(tracker-low)-1, tracker+1, high)
    return find_ith_elem_recursive(arr, i, 0, len(arr))

def test_ith_elem_one_entry():
    """
    Test to find the output when the array only contains one element
    """
    arr = [1]
    assert ith_elem(arr,0) == 1, \
        ("Array is %s, index is %s, Expected %s, but got %s"  
         %((', '.join(str(x) for x in arr)), 0, arr[0], ith_elem(arr,0)))
    
# test_ith_elem_one_entry()

def test_ith_elem_short_array():
    """
    Test to verify that the function throws an exception when the index is
    greater than number of elements. 
    """
    arr = [1]
    try:
        ith_elem(arr,1)
    except:
        pass
    else:
        raise ("Expected %s with index %s to hot an exception" 
               %((', '.join(str(x) for x in arr)), 1))
    
# test_ith_elem_short_array()

def test_ith_elem_arr_with_ten_elems():
    """
    Test to find the output when the array has predefined ten elements.
    """
    print("running")
    arr = [-7,6,8,2,5,9,0,5,1,8,12]
    index = 7
    elem = 8
    result = ith_elem(arr,index)
    assert result == elem, \
        ("Array is %s, index is %s, Expected %s, but got %s"  
         %((', '.join(str(x) for x in arr)), index, elem, result))
    
# test_ith_elem_arr_with_ten_elems() 

def test_ith_elem_arr_with_random_elems():
    """
    Test to find the output when the array contains
    random number of random numbers.
    """
    # Run the test 100 times.
    for _ in range(100):
        length = random.randint(1,100)
        arr = []
        for _ in range(length):
            arr.append(random.randint(-100,100))
        index = random.randint(0,length-1)
        result = ith_elem(arr,index)
        assert result == sorted(arr)[index], \
            ("Array is %s, index is %s, Expected %s, but got %s"  
         %((', '.join(str(x) for x in arr)), 
           index, sorted(arr)[index], result))
        
        
# test_ith_elem_arr_with_random_elems()       
    
       
            
        