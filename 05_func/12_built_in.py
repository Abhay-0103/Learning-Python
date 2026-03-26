def chai_flavor(flavor = "masala"):
    """Returns the flavor of chai."""
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)

help(len)


def generate_bill(chai=0, samosa=0, idli=0):
    """Generates a bill for the given items."""
    total = chai * 20 + samosa * 10 + idli * 15
    return total