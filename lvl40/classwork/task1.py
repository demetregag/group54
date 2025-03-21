def greet(name, surname, age, academy, favourite_color, city):
    return f"Hello, my name is {name}, my surname is {surname}. I am {age} years old. I study in {academy}. My favourite color is {favourite_color}. I live in {city}."

# ფუნქციის გამოძახება და შედეგის შენახვა ცვლადში
greeting = greet("John", "Doe", 20, "Tech Academy", "blue", "Tbilisi")

# შედეგის დაბეჭდვა
print(greeting)