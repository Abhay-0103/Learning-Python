def make_joke():
    yield "chick 1 : why did the chicken do the thing?"
    yield "chick 2 : because it was a chicken!"


joke = make_joke()

for chick in joke:
    print(chick)


def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function
def get_chai_generator():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


chai = get_chai_generator()
print(chai)
print(next(chai))