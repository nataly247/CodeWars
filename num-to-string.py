# Convert a Number to a String!

def number_to_string(num):
    string = str(num)
    return string

number_to_string(67)

# refactoring:
def number_to_string(num):
    return str(num)

# other interesting solutions

# incapsulation
def number_to_string(num):
    return "{}".format(num)

# lambda
number_to_string = lambda n: str(n)

# exeption
def number_to_string(num):
    try:
        return str(num)
    except:
        return None
