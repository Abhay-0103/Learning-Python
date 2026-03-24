def server_chai():
    chai_type = "Masala Chai" # Local Scops
    print(f"Inside FUncrtion {chai_type}")


chai_type = "Lemon"
server_chai()
print(f"Outside Function {chai_type}")


def chai_counter():
    chai_order = "Lemon" # Enclapsed Scops

    def print_order():
        chai_order = "gingeer"
        print(f"Inside Function {chai_order}")
    print("Outer: ", chai_order)
    print_order()