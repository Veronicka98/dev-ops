#8
def is_even(number):
    if number%2 == 1:
        return(False)
    else:
        return(True)

#9
def interval_intersect(a,b,c,d):
    return(not((b<c) or (d<a)))

#10
def name_and_age(name, age):
    if age < 0:
        return("Error: Invalid age")
    else:
        return("%s is %s years old" % (name, age))
