class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_Hot = True
print(Chai.is_Hot)

# Creting object from class in Chai

masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_Hot}")
masala.is_Hot = False

print("Chai: ",Chai.is_Hot)
print(f"Masala {masala.is_Hot}")

masala.flavor = "Masala"

print(masala.flavor)