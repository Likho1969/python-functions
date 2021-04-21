
# defining a function
def distance_from_zero(num):
    # passing an argument
    if type(num) == int:
        return abs(num)
    if type(num) == float:
        return abs(num)
    else:
        return "Nope"


# calling the pre-defined function
print(distance_from_zero(-5.6))
print(distance_from_zero("What"))




