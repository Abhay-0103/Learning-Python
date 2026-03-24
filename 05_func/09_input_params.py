love = "One Piece"

def love_finding(name):
    print("Finding love: ", name)

love_finding(love)
print("Love is: ", love)


# List

Hello = [1, 2, 3, 4, 5]

def edit_list(list): 
    list[1] = 0

edit_list(Hello)
print(Hello)


def make_love_strong(romance, lustfull, passion):
    print(romance, lustfull, passion)

make_love_strong("Of course", "Yes", "Always") #position based argument

# In keyword based argument
make_love_strong(romance="OHH YEAHHHHH", lustfull="FOR SURE", passion="ALWAYS TILL THE END") #keyword based argument



def special_person(*names, **new_ones):
    print("Names: ", names)
    print("New ones: ", new_ones)

special_person("Luffy", "Boa Hancock", only_fans_model="Nami", russian_baddie="Robin",)


def love_ones(person=[]):
    person.append("Luffy")
    print(person)

love_ones()
love_ones() # This will print the same list with "Luffy" twice because the


def love_ones(person=None):
    if person is None:
        person = []
    print(person) # This will print an empty list each time because a new list is created for each function call

love_ones()
love_ones() 