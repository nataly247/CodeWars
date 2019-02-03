def reverse(st):
    # split string to elements and convert it to a list
    st = st.split()   
    # result is ['Hello', 'World']
    
    # now we need to reverse the words order
    st = st[::-1]
    # result is ['World', 'Hello']
    
    # convert a list back to a string
        
    st = " ".join(st)
    # The join() method returns a string concatenated 
    # with the elements of an iterable (our list)
    
    return st

## other interesting solutions:

# reverse() method
def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)

# refactored
def reverse(st):
    return " ".join(reversed(st.split())).strip()
# strip() method 

