# pure function
def pure_chai(cups):
    return cups * 10

total_chai = 0


# impure function not recommanded
def impure_chai(cups):
    global total_chai
    total_chai += cups


# Recursive function
def pour_chai(n):
    print(n)
    if n ==0:
        return "All Cups are poured"
    return pour_chai(n-1)

print(pour_chai(3))


# Lambda function

chai_type = ["light", "medium", "strong"]

stromg_chai = list(filter(lambda chai: chai=="strong", chai_type))

print(stromg_chai)