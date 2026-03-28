class Chai:
    temperature = "Hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temperature) # Hot

cutting.temperature = "Mild"
print("After Changing ", cutting.temperature)
print("Direct look into the class", Chai.temperature) # Hot

del cutting.temperature
print("cutting.temperature after deleting ", cutting.temperature) # Hot