def have_a_love():
    # return "Love is in the air"
    print("Love is in the air") # This function will print the message but will return None by default

return_value = have_a_love()

print(return_value)

def last_love():
    pass

print(last_love()) # This will print None because the function does not return anything and pass is just a placeholder for future code.


def love_life():
    return "Love is complicated"

pyaar = love_life()
print(pyaar)

def love_status(she_left):
    if she_left == 0:
        return "Meekaaha , Madam Meowwww Gophhh Gophh Gophh"
    return "Tujhe jana hai toh jaa, mujhe ganta frak nahi padta hai"
    print("Tujhe ")

print(love_status(0))
print(love_status(1))


def love_report():
    return 100, 200 # This function returns a tuple with two values. The first value is 100 and the second value is 200.
sold, remain = love_report() # This will unpack the tuple returned by the love_report function into two variables, sold and remain.
print("Sold: ", sold)
print("Remain: ", remain)