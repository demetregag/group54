names = ["Ana", "Giorgi", "Nino", "Alex", "David", "Elene", "Luka", "Saba", "Anna", "Irakli"]
renewed = [name for name in names if len(name) < 6 or name.startswith("A")]
print(renewed)