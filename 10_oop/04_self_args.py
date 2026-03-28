class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml cup of chai."
    

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
print(Chaicup.describe(cup_two))