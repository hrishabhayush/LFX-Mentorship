def innovateList(myList):
    '''
    Returns a list of integers based on the input list.

    This function returns a list of integers but with items at positions which are
    multiples of 2 or 3 removed. The function emits an error message if the input list
    is not a multiple of 10.

    Parameter myList: the list to check
    Precondition: myList must be a list.
    '''
    if len(myList) == 0:
        return []
    
    if len(myList) % 10 != 0:
        raise ValueError("Input list is not a multiple of 10")
    
    try:
        new_list = []
        for i in range(len(myList)):
            if i % 2!=0 and i % 3 !=0:
                new_list.append(myList[i])
        return new_list
        
    except ValueError as e:
        print(f"Error: {e}")
