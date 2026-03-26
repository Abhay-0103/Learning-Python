favourite_types = [
    "Romance",
    "sexy",
    "Hottest",
    "Love",
    "Romantic",
    "lustful",
]

unique_mohabbat = {Pyaar for Pyaar in favourite_types}
print(unique_mohabbat)



Cooking_Pyaar = {
    "Pyaar": ["lustful", "Sex", "Romance"],
    "Mohabbat": ["Hottest", "Love", "Romantic"],
    "MakeOut": ["sexy", "Romance", "Love"],
}

unique_Prethi = {type for ingredient in Cooking_Pyaar.values() for type in ingredient}
print(unique_Prethi)