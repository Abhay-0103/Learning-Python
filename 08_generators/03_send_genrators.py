def chai_customer():
    print("Kaha ho , lala")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield


customer = chai_customer()
next(customer) # Start the generator
customer.send("Masala Chai")